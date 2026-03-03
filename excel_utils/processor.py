from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calculate_nights_per_date_range(year, month, data):
    nights_per_date_range = []

    for row in data:
        arrival_date = row[1]
        leaving_date = row[2]

        if leaving_date >= datetime(year, month, 1) and arrival_date <= datetime(year, month, 1) + relativedelta(months=1, days=-1):
            start_date = datetime(year, month, 1)
            if month == 12:
                end_date = datetime(year+1, 1, 1) - timedelta(days=1)
            else:
                end_date = datetime(year, month+1, 1) - timedelta(days=1)

            nights = (min(end_date, leaving_date) - max(start_date, arrival_date)).days + 1

            if leaving_date.month == month and leaving_date.year == year:
                nights -= 1

            key = f'{arrival_date.date()} - {leaving_date.date()}'

            if 'Owner' in row or 'Čiščenje / hišnik' in row:
                nights = 0
                key += ' (Owner)' if 'Owner' in row else ' (Čiščenje / hišnik)'

            nights_per_date_range.append((key, nights))

        else:
            key = f'{arrival_date.date()} - {leaving_date.date()}'

            if 'Owner' in row or 'Čiščenje / hišnik' in row:
                key += ' (Owner)' if 'Owner' in row else ' (Čiščenje / hišnik)'
            
            nights_per_date_range.append((key, 0))
    return nights_per_date_range
