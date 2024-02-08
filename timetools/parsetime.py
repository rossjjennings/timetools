from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from tzlocal import get_localzone

def datetime_from_args(args, default_tz=None):
    try:
        tz = ZoneInfo(args[-1])
        args.pop()
    except ZoneInfoNotFoundError:
        tz = get_localzone() if default_tz is None else default_tz

    timestr = 'T'.join(args)
    if not '-' in timestr:
        # we weren't given a date, assume it's today
        now = datetime.now().astimezone(default_tz)
        if timestr == 'now':
            return now
        else:
            timestr = f"{now.year}-{now.month}-{now.day}T{timestr}"

    if not ':' in timestr:
        # we weren't given a time, assume 00:00
        time = datetime.strptime(timestr, "%Y-%m-%d")
    elif ':' in timestr and not '.' in timestr:
        # there's no fractional second
        try:
            time = datetime.strptime(timestr, "%Y-%m-%dT%H:%M")
        except ValueError:
            time = datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S")
    elif ':' in timestr and '.' in timestr:
        # there is a fractional second
        time = datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S.%f")
    else:
        raise ValueError(f"could not interpret '{' '.join(args)}' as a time")

    time = time.replace(tzinfo=tz)
    return time
    
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("time", nargs='+', help="Time (YYYY-MM-DD [HH:MM:SS[.f]] [TZ])")
    args = parser.parse_args()

    time = datetime_from_args(args.time)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S %Z%z')} [{time.tzinfo}]")
