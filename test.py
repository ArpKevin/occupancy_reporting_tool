from file_utils.validator import get_file_name_cli
from excel_utils.reader import load_workbook, extract_valid_rows
from excel_utils.processor import calculate_nights_per_date_range

def get_user_year():
    while True:
        try:
            year = int(input("Enter the year (YYYY): "))
            if 10000 > year > 999:
                return year
            else:
                print("Please enter a number between 1000 and 9999.")
        except ValueError:
            print("Please enter a valid number.")

def get_user_month():
    while True:
        try:
            month = int(input("Enter the month (MM): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")

def insert_nights(year, month, nights_per_date_range, ws, wb, file_name):
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

    x = 2
    for date_range, nights in nights_per_date_range:
        ws[f"K{x}"].value = nights
        x+=1

    wb.save(file_name)

    input("\nData inserted successfully.")

def main():
    file_name = get_file_name_cli()
    wb, ws = load_workbook(file_name)
    data = extract_valid_rows(ws)
    year = get_user_year()
    month = get_user_month()
    nights_per_date_range = calculate_nights_per_date_range(year, month, data)
    insert_nights(year, month, nights_per_date_range, ws, wb, file_name)

if __name__ == "__main__":
    main()