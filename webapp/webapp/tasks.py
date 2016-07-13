from __future__ import absolute_import
from webapp.celery import app
import time


@app.task
def add(x, y):
	time.sleep(5)
	return x + y
    