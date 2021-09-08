from datetime import datetime
import pytz

timezone_moscow = pytz.timezone('Europe/Moscow')


def get_date():
    return datetime.now(timezone_moscow)


if __name__ == "__main__":
   print(get_date())