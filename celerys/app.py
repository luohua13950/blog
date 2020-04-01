from __future__ import absolute_import
from celery import Celery

app = Celery("tasks")
app.config_from_object('celerys.celeryconfig', namespace='CELERY')