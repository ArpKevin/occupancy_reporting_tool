import openpyxl
from dateutil.parser import parse
from datetime import datetime

def load_workbook(file_name):
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active
    return wb, ws

def is_valid_date(item):
    if isinstance(item, datetime):
        return True
    elif isinstance(item, str):
        try:
            parse(item)
            return True
        except (ValueError, TypeError):
            return False
    return False

def extract_valid_rows(ws):
    data = []
    for row in ws.iter_rows(values_only=True):
        if any(is_valid_date(item) for item in row):
            data.append(row)
    return data