from datetime import datetime
from zoneinfo import ZoneInfo
from tzlocal import get_localzone
from astropy.time import Time
from timetools.parsetime import datetime_from_args

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("time", nargs='*', default=['now'], help="time (YYYY-MM-DD [HH:MM:SS[.f]] TZ)")
    args = parser.parse_args()
    
    try:
        mjd = float(args.time[0])
    except ValueError:
        time = Time(datetime_from_args(args.time))
        print(f"{time.mjd:.11g}")
    else:
        time = Time(mjd, format="mjd")
        dt = time.datetime.replace(tzinfo=ZoneInfo("UTC"))
        print(dt.strftime("%Y-%m-%d %H:%M:%S %Z"))

if __name__ == '__main__':
    main()
