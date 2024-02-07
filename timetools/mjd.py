from datetime import datetime
from zoneinfo import ZoneInfo
from tzlocal import get_localzone
from astropy.time import Time
from timetools.parsetime import datetime_from_args

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--local", action='store_true',
                        help="work in local time zone by default (otherwise, default to UTC)")
    parser.add_argument("time", nargs='*', default=['now'], help="time (YYYY-MM-DD [HH:MM:SS[.f]] TZ)")
    args = parser.parse_args()

    if args.local:
        default_tz = get_localzone()
    else:
        default_tz = ZoneInfo("UTC")
    
    try:
        mjd = float(args.time[0])
    except ValueError:
        time = Time(datetime_from_args(args.time, default_tz=default_tz))
        print(f"{time.mjd:.11g}")
    else:
        time = Time(mjd, format="mjd")
        dt = time.datetime.replace(tzinfo=ZoneInfo("UTC"))
        dt = dt.astimezone(default_tz)
        if not args.local and mjd % 1 == 0:
            print(dt.strftime("%Y-%m-%d"))
        else:
            print(dt.strftime("%Y-%m-%d %H:%M:%S %Z"))

if __name__ == '__main__':
    main()
