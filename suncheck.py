import config
import urllib
import json
import datetime
import time


def check_sun():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    now = datetime.datetime.now()
    now_unix = int(time.mktime(datetime.datetime.now().timetuple()))

    url = "https://api.sunrise-sunset.org/json?lat=" + config.LAT + \
          "&lng=" + config.LNG + "&formatted=0"
    response = urllib.urlopen(url)
    today = json.loads(response.read())

    url = "https://api.sunrise-sunset.org/json?lat=" + config.LAT + \
          "&lng=" + config.LNG + "&formatted=0&date=" + str(tomorrow)
    response = urllib.urlopen(url)
    tomorrow = json.loads(response.read())

    today_rise = datetime.datetime.strptime(today["results"]["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
    today_set = datetime.datetime.strptime(today["results"]["civil_twilight_end"], "%Y-%m-%dT%H:%M:%S+00:00")
    tomorrow_rise = datetime.datetime.strptime(tomorrow["results"]["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
    tomorrow_set = datetime.datetime.strptime(tomorrow["results"]["civil_twilight_end"], "%Y-%m-%dT%H:%M:%S+00:00")

    sleep = None
    wake_time = None

    if now > today_set:
        # Sleep until tomorrows sunrise
        wake_time = tomorrow["results"]["civil_twilight_begin"]
        wake = datetime.datetime.strptime(tomorrow["results"]["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
        wake_unix = int(time.mktime(wake.timetuple()))
        sleep = wake_unix - now_unix
    if now < today_rise:
        # Sleep until todays sunrise
        wake_time = today["results"]["civil_twilight_begin"]
        wake = datetime.datetime.strptime(today["results"]["civil_twilight_begin"], "%Y-%m-%dT%H:%M:%S+00:00")
        wake_unix = int(time.mktime(wake.timetuple()))
        sleep = wake_unix - now_unix

    if sleep:
        print("Sleeping for " + str(sleep) + " + 1 seconds, until " + str(wake_time))
        sleep = sleep + 1
        time.sleep(sleep)
        check_sun()


if __name__ == '__main__':
    check_sun()
