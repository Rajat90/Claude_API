import datetime
def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S2"):
     if not date_format:
          raise ValueError("Date format cannot be empty.")
     return datetime.now().strftime(date_format) 