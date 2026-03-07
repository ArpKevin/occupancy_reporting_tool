import calendar

def insert_nights(year, month, nights_per_date_range, ws, wb, file_name):
    month_name = calendar.month_name[month]

    ws["K1"].value = f"Nights in month ({year} {month_name})"

    x = 2
    for nights in nights_per_date_range:
        ws[f"K{x}"].value = nights
        x+=1

    wb.save(file_name)