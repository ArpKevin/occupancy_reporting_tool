import openpyxl
import os.path
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

while True:
    file_name = input("Enter the name of the xlsx file: ")

    if not file_name.endswith(".xlsx"):
        file_name += ".xlsx"

    if os.path.isfile(file_name):
        break
    else:
        print("Invalid file name. Try again.")

wb = openpyxl.load_workbook(file_name)
ws = wb.active

data = []
for row in ws.iter_rows(values_only=True):
    is_valid_date = False
    for item in row:
        if isinstance(item, str):
            try:
                datetime.strptime(item, '%m/%d/%Y')
                is_valid_date = True
                break
            except ValueError:
                pass
        elif isinstance(item, datetime):
            is_valid_date = True
            break
    if is_valid_date:
        data.append(row)

while True:
    try:
        year = int(input("Enter the year (YYYY): "))
        if 10000 > year > 999:
            break
        else:
            print("Please enter a number between 1000 and 9999.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        month = int(input("Enter the month (MM): "))
        if 1 <= month <= 12:
            break
        else:
            print("Please enter a number between 1 and 12.")
    except ValueError:
        print("Please enter a valid number.")

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



print(f"\nNights spent in {month}/{year}:")
total_nights = 0
for date_range, nights in nights_per_date_range:
    print(f"{date_range}: {nights}")
    total_nights += nights
print(f"Total nights: {total_nights}")

input("\nPress \"Enter\" to insert the values into the xlsx...")

print("Please wait. This may take a few seconds...")

month_name = "January" if month == 1 else \
             "February" if month == 2 else \
             "March" if month == 3 else \
             "April" if month == 4 else \
             "May" if month == 5 else \
             "June" if month == 6 else \
             "July" if month == 7 else \
             "August" if month == 8 else \
             "September" if month == 9 else \
             "October" if month == 10 else \
             "November" if month == 11 else \
             "December"

ws["K1"].value = f"Nights in month ({year} {month_name})"

for row in ws.iter_rows(min_row=2):

    key = f'{row[1].value} - {row[2].value}'

    x = 2
    for date_range, nights in nights_per_date_range:
        ws[f"K{x}"].value = nights
        x+=1


wb.save(file_name)

input("\nData inserted successfully.")