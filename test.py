from file_utils.validator import get_file_name_cli
from excel_utils.reader import load_workbook, extract_valid_rows
from excel_utils.processor import calculate_nights_per_date_range, get_month_range
from excel_utils.writer import insert_nights

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

def main():
    file_name = get_file_name_cli()
    wb, ws, headers = load_workbook(file_name)
    data = extract_valid_rows(ws, headers)
    year = get_user_year()
    month = get_user_month()
    start_date, end_date = get_month_range(year, month)
    nights_per_date_range = calculate_nights_per_date_range(data, headers, start_date, end_date, year, month)
    insert_nights(nights_per_date_range, ws, wb, file_name, headers)

if __name__ == "__main__":
    main()