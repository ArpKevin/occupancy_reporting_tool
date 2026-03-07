from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_month_range(year, month):
    start_date = datetime(year, month, 1)
    end_date = start_date + relativedelta(months=1) - timedelta(days=1)
    return start_date, end_date

def is_within_range(arrival_date, leaving_date, start_date, end_date):
    return leaving_date >= start_date and arrival_date <= end_date

def calculate_nights_per_date_range(data, headers, start_date, end_date, year, month):
    nights_per_date_range = []

    idx_arrival_date = headers.index("Date from")
    idx_leaving_date = headers.index("Date until")

    for row in data:
        arrival_date = row[idx_arrival_date]
        leaving_date = row[idx_leaving_date]

        if is_within_range(arrival_date, leaving_date, start_date, end_date):
            nights = (min(end_date, leaving_date) - max(start_date, arrival_date)).days + 1

            if leaving_date.month == month and leaving_date.year == year:
                nights -= 1

            if 'Owner' in row or 'Čiščenje / hišnik' in row:
                nights = 0

            nights_per_date_range.append(nights)
        else:        
            nights_per_date_range.append(0)
    return nights_per_date_range
