from datetime import datetime
import pytz

timezone_moscow = pytz.timezone('Europe/Moscow')


def get_date():
    return datetime.gmtnow(timezone_moscow)


if __name__ == "__main__":
    pass
   # print(current_date)