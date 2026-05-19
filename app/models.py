from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    reset_token = fields.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return self.name
    
class Question(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    user = fields.ForeignKeyField('models.User', related_name='questions')
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Result(Model):
    id = fields.IntField(pk=True)
    question = fields.ForeignKeyField('models.Question', related_name='results')
    answer = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Result for {self.question.title}"