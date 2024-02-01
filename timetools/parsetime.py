import pytz

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("time", nargs='+', help="Time in ISO format with optional tz database time zone")
    args = parser.parse_args()

    print(args.time[0])
