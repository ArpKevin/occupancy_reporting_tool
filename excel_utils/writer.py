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
    for nights in nights_per_date_range:
        ws[f"K{x}"].value = nights
        x+=1

    wb.save(file_name)

    input("\nData inserted successfully.")
