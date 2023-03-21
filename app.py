import pywhatkit
import schedule
import time

phone = "+9005550000000"
message = "Test"

def job() :
    pywhatkit.sendwhatmsg(phone,message,int(time.strftime("%H",time.localtime())),int(time.strftime("%M",time.localtime()))+1,10,True,3)

schedule.every(10).seconds.do(job)

while True :
    schedule.run_pending()
    time.sleep(1)