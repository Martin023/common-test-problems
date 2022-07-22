import datetime as dt

def get_date():
    """
    Get the current date and return it as a string.
    """
    today = dt.date.today()
    # print(today.strftime("%d/%m/%Y"))
    print(today)
get_date()