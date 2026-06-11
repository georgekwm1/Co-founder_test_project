from app.main import app
from app.config import settings
from groq import Groq
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth_utility import *
from app.models import User, Question, Result
from pydantic import BaseModel, EmailStr
from app.tasks import send_reset_email
from fastapi import BackgroundTasks
import secrets
import json

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=settings.algorithm)
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await User.get(email=email)  # or fetch user from DB here
    return user




class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    token: str
    new_password: str
    confirm_password: str

class AIInstructionsRequest(BaseModel):
    question: str

@app.post("/signup")
async def signup(data: SignupRequest):
    try:
        existing_user = await User.filter(email=data.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = hash_password(data.password)
        user = User(name=data.name, email=data.email, password=hashed_password)
        await user.save()
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/forgot-password")
async def forgot_password(data: ForgotPasswordRequest, background_tasks: BackgroundTasks):
    try:
        user = await User.filter(email=data.email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # Here you would generate a password reset token and send an email to the user
        token = secrets.token_hex(8)  # Replace with actual token generation logic
        user.reset_token = token
        await user.save()
        # send_reset_email.delay(data.email, token)
        background_tasks.add_task(send_reset_email, data.email, token)
        return {"message": "Password reset instructions sent to your email"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/reset-password")
async def reset_password(data: ResetPasswordRequest):
    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    try:
        user = await User.filter(email=data.email).first()
        if not user or user.reset_token != data.token:
            raise HTTPException(status_code=400, detail="Invalid token or email")
        user.password = hash_password(data.new_password)
        user.reset_token = None
        await user.save()
        return {"message": "Password reset successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
async def login(data: LoginRequest):
    try:
        user = await User.filter(email=data.email).first()
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        access_token = create_access_token(data={"email": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/instructions")
async def instructions(data: AIInstructionsRequest, current_user: User = Depends(get_current_user)):
    question = data.question
    # Here you would process the AI instructions based on the provided context
    client = Groq(api_key=settings.api_key)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates interview question based on the provided job title or role. Return strictly 3 thoughtful interview questions specific to that role questions in a JSON array format without any additional text. If any other questions are asked, respond with 'Please provide a job title or role to generate interview questions.'"
            },
          {
            "role": "user",
            "content": f"{question}"
          }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )

    chunks = [chunk.choices[0].delta.content or "" for chunk in completion]
    full_response = "".join(chunks)
    print(f"Generated interview questions:\n{full_response}")
    try:
        parsed = json.loads(full_response)
        question_obj = Question(title=f"Interview questions for {question}", description=question, user=current_user)
        await question_obj.save()
        result = Result(question=question_obj, answer=json.dumps(parsed))
        await result.save()
    except json.JSONDecodeError:
        parsed = []
    return {"message": "Response processed", "response": parsed}

@app.get("/search_history")
async def search_history(current_user: User = Depends(get_current_user)):
    questions = await Question.filter(user=current_user).prefetch_related("results")
    history = []
    for q in questions:
        results = await q.results.all()
        history.append({
            "question": q.description,
            "results": [item for r in results for item in json.loads(r.answer)]
        })
    return {"history": history}

# @app.delete("/clear_history")
# async def clear_history(current_user: User = Depends(get_current_user)):
#     questions = await Question.filter(user=current_user).all()
#     for q in questions:
#         await q.delete()
#     return {"message": "Search history cleared"}
