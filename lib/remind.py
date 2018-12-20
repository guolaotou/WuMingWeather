import schedule
import time, os, yaml
from send_email_lib import Email
from spider_moji import Splider

filename = os.path.join(os.path.dirname(__file__), '../config.yaml').replace("\\", "/")
with open(filename) as f:
    config = yaml.load(f)
setting_morning = config.get("main").get("remind_time").get("morning")
setting_evening = config.get("main").get("remind_time").get("evening")

print("setting_morning", setting_morning)
print("setting_evening", setting_evening)

def job():
    print("I'm working...")

def remind():
    spider = Splider()
    temperature = spider.get_temperature()
    print("temperature", temperature)
    wind = spider.get_wind()
    aqi = spider.get_aqi()
    text = "\n".join([temperature, wind, aqi])

    email = Email()
    email.send_email(text)

schedule.every().day.at(setting_morning).do(remind)
schedule.every().day.at(setting_evening).do(job)


if __name__ == "__main__":
    # remind()
    while True:
        schedule.run_pending()
        time.sleep(1)

