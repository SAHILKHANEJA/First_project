from __future__ import absolute_import
from webapp.celery import app
import time
import requests

@app.task
def add(x, y):
	time.sleep(5)
	return x + y
	
@app.task
def send_simple_message():
    print("sending mail")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5a65807b964a4cec849664c61333947c.mailgun.org/messages",
        auth=("api", "key-36b28df15f69e2dccf5f5f50d5e16957"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox5a65807b964a4cec849664c61333947c.mailgun.org>",
              "to": "Sahil Khaneja <sahilkhaneja78@gmail.com>",
              "subject": "Hello Sahil Khaneja",
              "text": "Congratulations Sahil Khaneja, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})      
    