from dotenv import load_dotenv
import os

load_dotenv()

ARRIVAL_HEADER = os.getenv("ARRIVAL_HEADER")
LEAVING_HEADER = os.getenv("LEAVING_HEADER")
RENT_HEADER = os.getenv("RENT_HEADER")
SPECIAL_GUESTS = os.getenv("SPECIAL_GUESTS")
SPECIAL_GUESTS = SPECIAL_GUESTS.split(",") if SPECIAL_GUESTS else []