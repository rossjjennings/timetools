from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from tzlocal import get_localzone

def time_from_args(args):
    try:
        tz = ZoneInfo(args[-1])
        args.pop()
    except ZoneInfoNotFoundError:
        tz = get_localzone()

    timestr = 'T'.join(args)
    if timestr == 'now':
        time = datetime.now()
    else:
        try:
            time = datetime.strptime(timestr, "%Y-%m-%d")
        except ValueError:
            try:
                time = datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                time = datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S.%f")

    time = time.replace(tzinfo=tz)
    return time
    
    raise ValueError(f"Could not interpret '{' '.join(args)}' as a time")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("time", nargs='+', help="Time (YYYY-MM-DD [HH:MM:SS[.f]] [TZ])")
    args = parser.parse_args()

    time = time_from_args(args.time)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S %Z')} [{time.tzinfo}]")
