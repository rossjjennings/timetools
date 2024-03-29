from zoneinfo import ZoneInfo
from timetools.parsetime import datetime_from_args

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true', help="display additional information about time zone on output")
    parser.add_argument("time", nargs='+', help="time (YYYY-MM-DD [HH:MM:SS[.f]] TZ)")
    parser.add_argument("newzone", help="new time zone (IANA tz database key)")
    args = parser.parse_args()

    time = datetime_from_args(args.time)
    newzone = ZoneInfo(args.newzone)
    time = time.astimezone(newzone)
    if args.verbose:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S %Z%z')} [{time.tzinfo}]")
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S %Z'))

