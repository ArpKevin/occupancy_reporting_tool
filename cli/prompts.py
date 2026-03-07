from file_utils.validator import validate_file

def validate_value(num, min_value, max_value):
    return min_value <= num <= max_value

def get_user_year():
    while True:
        try:
            year = int(input("Enter the year (YYYY): "))
            if validate_value(year, 1000, 9999):
                return year
            else:
                print("Please enter a number between 1000 and 9999.")
        except ValueError:
            print("Please enter a valid number.")

def get_user_month():
    while True:
        try:
            month = int(input("Enter the month (MM): "))
            if validate_value(month, 1, 12):
                return month
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")

def get_file_name_cli():
    while True:
        user_input = input("Enter the name of the xlsx file: ")
        file_name = validate_file(user_input)
        if file_name:
            return file_name
        else:
            print("Invalid file name. Try again.")