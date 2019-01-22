MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

REFYEAR = 1700
REFMONTH = 1
REFDAY = 1
REFDAY_OF_WEEK = FRIDAY

MONTHS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def is_leap_year(year):
    if year < 1700:
        raise Exception('Calendar unsupported for dates before 1700')
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def get_months(year):
    if is_leap_year(year):
        months = MONTHS.copy()
        months.update({2: 29})
        return months
    else:
        return MONTHS.copy()

def format_date(year, month, day):
    return "{}-{:02d}-{:02d}".format(year, month, day)

def get_date_from_day(day_in_year, year):
    months = get_months(year)
    days_left = day_in_year
    for m in range(1, 13):
        if days_left <= months[m]:
            return format_date(year, m, days_left)
        days_left -= months[m]

def get_day_of_year(year, month, day):
    months = get_months(year)
    for m in range(1, month):
        day += months[m]
    return day

def get_days_since_reference_date(year, month, day):
    days = get_day_of_year(year, month, day) - 1
    for y in range(REFYEAR, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365
    return days

def get_days_between(year1, month1, day1, year2, month2, day2):
    d1 = get_days_since_reference_date(year1, month1, day1)
    d2 = get_days_since_reference_date(year2, month2, day2)
    return d2 - d1

def get_day_of_week(year, month, day):
    days = get_days_since_reference_date(year, month, day)
    days += REFDAY_OF_WEEK
    return days % 7

def get_day_position(day_of_week, start_of_week):
    return (day_of_week + 7 - start_of_week) % 7

def make_calendar_month_array(year, month, start_of_week=MONDAY):
    months = get_months(year)
    calendar_month = []
    first_day = get_day_of_week(year, month, 1)
    first_day_position = get_day_position(first_day, start_of_week)
    week = []
    for i in range(first_day_position):
        # fill in empty spaces before first day
        week.append("")

    for d in range(1, months[month] + 1):
        week.append(d)
        if len(week) == 7:
            calendar_month.append(week)
            week = []
    if week:
        calendar_month.append(week)

    return calendar_month

PAD_LEFT = 1
PAD_RIGHT = 2

def format_as_string(i, min_length=0, pad_type=PAD_LEFT, pad_char=" "):
    s = str(i)
    while len(s) < min_length:
        if PAD_LEFT:
            s = pad_char + s
        else:
            s = s + pad_char
    return s

def format_calendar_array(month):
    return "\n".join([
        " ".join(format_as_string(d, min_length=2) for d in w)
        for w in month
    ])

print format_calendar_array(make_calendar_month_array(2019, 1, start_of_week=SUNDAY))

assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(1996) == True
assert is_leap_year(2020) == True
assert is_leap_year(2001) == False

assert get_days_since_reference_date(REFYEAR, REFMONTH, REFDAY) == 0
assert get_days_since_reference_date(REFYEAR, REFMONTH, REFDAY + 1) == 1
assert get_days_since_reference_date(REFYEAR, REFMONTH + 1, REFDAY + 1) == 32
assert get_days_since_reference_date(REFYEAR + 1, REFMONTH, REFDAY) == 365

assert get_day_of_week(REFYEAR, REFMONTH, REFDAY) == REFDAY_OF_WEEK
assert get_day_of_week(1988, 4, 13) == WEDNESDAY

assert format_date(2003, 1, 5) == "2003-01-05"
