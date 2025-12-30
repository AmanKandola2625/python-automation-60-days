import argparse
from datetime import date, timedelta


def eta_for_day(current_completed_day: int, total_days: int = 60, pace_days_per_day: float = 1.0):
    remaining = total_days - current_completed_day
    # If you complete 1 day per day, remaining days = remaining
    # If pace is 0.5 (one day every 2 days), it takes remaining / 0.5
    days_needed = int((remaining / pace_days_per_day) + 0.999999)  # ceiling
    finish = date.today() + timedelta(days=days_needed)
    return remaining, finish


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--completed", type=int, required=True, help="Last completed day number (e.g., 36)")
    ap.add_argument("--pace", type=float, default=1.0, help="Days per day (1.0 = one per day)")
    args = ap.parse_args()

    remaining, finish = eta_for_day(args.completed, total_days=60, pace_days_per_day=args.pace)
    print(f"Completed: Day {args.completed}")
    print(f"Remaining days: {remaining}")
    print(f"Estimated finish date (pace={args.pace}): {finish.isoformat()}")


if __name__ == "__main__":
    main()
