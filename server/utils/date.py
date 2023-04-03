from datetime import datetime

DATE_REGEX = "^\w{3}\s\d{1,2}\/\d{1,2}$"


def generate_date_regex(date):
    return datetime.strftime(date, "^\w{3}\s%-m/%-d$")


def get_current_year():
    now = datetime.now().year
    return str(now)


def get_christmas_date():
    return datetime(year=int(get_current_year()), month=12, day=25)


def get_new_years_date():
    return datetime(year=int(get_current_year()), month=1, day=1)


def get_valentines_date():
    return datetime(year=int(get_current_year()), month=2, day=14)
