import time

from django.core.mail import send_mail

from api.views import dataSend, username, email
import schedule

defaultData=0
name=''
def reminder():
    data=dataSend
    iteam=(data.items())
    global defaultData
    defaultData=iteam


def reminder2():
    send_mail(
        "time for medicine",
        f"hello mr {username} this is time for your medicine {name}",
        "2018pcemerohit58@poornima.org",
        [email],
        fail_silently=False,
    )


def reminder1():
    reminder()
    data=defaultData
    for i in data:
        s=str(i[1])
        global name
        name=str(i[0])
        schedule.every().day.at(str(s)).do(reminder2)


schedule.every(1).minutes.do(reminder1)

def warning():
    send_mail(
        "count the madicins",
        f"hello mr/mrs. {username}  this is an allart for you plese check your madician stock and if it is going to finish plese purchase them and this is also an alart for helth chackup plese shadule your monthely helth chackup",
        "2018pcemerohit58@poornima.org",
        [email],
        fail_silently=False,
    )


schedule.every(28).days.do(warning)


while True:
    schedule.run_pending()
    time.sleep(1)
