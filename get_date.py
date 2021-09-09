from datetime import datetime
import pytz


timezone_moscow = pytz.timezone('Europe/Moscow')


def get_week_num():
    september = datetime(2021, 9, 1)
    now = datetime.now(timezone_moscow)
    return now.isocalendar()[1] - september.isocalendar()[1]


def get_week_day():
    return datetime.now(timezone_moscow).isoweekday()

if __name__ == "__main__":
   print(get_week_day())