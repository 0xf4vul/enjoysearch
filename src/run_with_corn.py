# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
from news import save_to_html

path = os.path.dirname(os.path.realpath(__file__))

# scheduler = BlockingScheduler()
scheduler = BackgroundScheduler

def job():
    print("execute news to html")
    save_to_html()
    # print "%s: 执行任务"  % time.asctime()

# scheduler.add_job(job, 'interval', seconds=30)
scheduler.add_job(job, 'interval', hours=3)

scheduler.start()

while True:
    pass
    
# hour =19 , minute =23
# hour ='19', minute ='23'
# minute = '*/3' 表示每 5 分钟执行一次
# hour ='19-21', minute= '23' 表示 19:23、 20:23、 21:23 各执行一次任务
