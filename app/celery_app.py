from celery import Celery
from app.config import settings
from celery.schedules import crontab

celery = Celery(
    "worker",
    broker=settings.redis_url,       # e.g. "redis://localhost:6379/0"
    backend=settings.redis_url,
    include=["app.tasks"]             # modules where tasks live
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)

# celery.conf.beat_schedule = {
#     "run-every-morning": {
#         "task": "app.tasks.some_background_job",
#         "schedule": crontab(hour=8, minute=0),  # every day at 8am
#     },
# }