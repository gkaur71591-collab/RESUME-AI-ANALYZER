from celery import Celery


celery_app = Celery(
    "resume_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=[
        "app.worker.tasks"
    ]
)


celery_app.conf.update(
    task_track_started=True
)