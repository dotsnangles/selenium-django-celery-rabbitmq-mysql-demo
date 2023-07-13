from datetime import datetime, time, timedelta
import pytz


def get_yesterday():
    seoul_tz = pytz.timezone("Asia/Seoul")
    datetime_in_seoul = datetime.now(tz=pytz.utc).astimezone(seoul_tz)

    start_time = time(0, 0, 0)
    end_time = time(0, 0, 6)

    time_in_seoul = datetime_in_seoul.time()

    if time_in_seoul >= start_time and time_in_seoul <= end_time:
        yesterday = (datetime_in_seoul - timedelta(days=1)).date().strftime("%Y%m%d")
        return yesterday, True
    else:
        return None, False
