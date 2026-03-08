from config import ARRIVAL_HEADER, LEAVING_HEADER, RENT_HEADER, SPECIAL_GUESTS

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_month_range(year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date + relativedelta(months=1) - timedelta(days=1)
    return start_date, end_date

def is_within_range(arrival_date, leaving_date, start_date, end_date):
    return leaving_date >= start_date and arrival_date <= end_date

def is_special_guest(guest_name):
    return guest_name in SPECIAL_GUESTS

def calculate_nights_per_date_range(data, headers, start_date, end_date, year, month):
    nights_per_date_range = []

    idx_arrival_date = headers.index(ARRIVAL_HEADER)
    idx_leaving_date = headers.index(LEAVING_HEADER)
    idx_rent_source = headers.index(RENT_HEADER)

    for row in data:
        arrival_date = row[idx_arrival_date]
        leaving_date = row[idx_leaving_date]
        guest_name = row[idx_rent_source]

        if is_special_guest(guest_name):
            nights_per_date_range.append(0)
            continue

        if not is_within_range(arrival_date, leaving_date, start_date, end_date):
            nights_per_date_range.append(0)
            continue

        # Calculate overlapping nights
        nights = (min(end_date, leaving_date) - max(start_date, arrival_date)).days + 1

        # Subtract one night if the leaving date is in the checked month
        if leaving_date.year == year and leaving_date.month == month:
            nights -= 1

        nights_per_date_range.append(nights)
    return nights_per_date_range
