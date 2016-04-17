from datetime import date, datetime, time, timedelta

from django.contrib import messages

from terms.models import Term

def date_for_day_of_week(date, day):
    """ returns the date of the specified day in the week identifid by date.
        For example, if date 4/9/2016 (Saturday) and 0 (Monday) are passed in,
        4/4/2016 will be returned. """
    return datetime.combine(date + timedelta(days=day-date.weekday()), time(0,0))

def term_start_date_from_semiannual(season, year):
    """ This returns the best-guess term start date for the given semi-annual.
        Input should follow teh form of ("Winter"/"Summer", year) """
    if season == "Winter":
        seed_date = datetime(year, 12, 25)
    else:
        seed_date = datetime(year, 7, 4)

    # Make it a Monday
    seed_date = date_for_day_of_week(seed_date, 0)

    # return date of 19 weeks previous-- one week for semi-annual
    return datetime.combine(seed_date + timedelta(weeks=-19, days=0), time(0,0)).date()

def next_term_start_date(date):
    """ returns the next possible start term date (best guess)"""

    # Not really worth it to be smart here--just start in Spring of this year and keep 
    # going until we have a workable date.
    season = "Summer"
    year = date.year

    while True:
        start_date = term_start_date_from_semiannual(season, year)

        # give a week lee-way in case we guessed the wrong semi-annual week
        if (start_date + timedelta(7)) > date:
            return start_date

        # increment semiannual
        if season == "Summer":
            season = "Winter"
        else:
            season = "Summer"
            year = year + 1

def previous_term():
    current_term = Term.current_term()
    if current_term != None:
        return current_term.season, current_term.year

    return None, None

def generate_term():
    season, year = previous_term()

    if season == "Fall":
        season = "Spring"
        year = year + 1
    elif season == "Spring":
        season = "Fall"
    else:
        # No term found, use today's date to identify what term we are hoping to create
        today = datetime.now().date()
        start_date = next_term_start_date(today)
        if start_date.month <= 4:  # month chosen semi-arbitrarily
            return "Spring", start_date.year
        else:
            return "Fall", start_date.year

    return (season, year)

def validate_term(start, end, c_init, c_grace, c_periods, c_totalweeks, request):
    """ Validates the provided information.  Returns true/false based
        on the validity of the data """

    success = True

    # Start needs to be a Monday and end needs to be a Sunday
    if start.weekday() != 0:
        messages.add_message(request, messages.ERROR, 
            'Term start date needs to be a Monday.')
        success = False

    if end.weekday() != 6:
        messages.add_message(request, messages.ERROR, 
            'Term end date needs to be a Lord\'s Day.')
        success = False

    if (end - start).days != (7 * c_totalweeks - 1):
        messages.add_message(request, messages.ERROR, 
            'Term length does not match requested number of weeks (' + str(c_totalweeks) + ').')
        success = False

    if (int(c_init) + int(c_grace) + int(c_periods) * 2) != c_totalweeks:
        messages.add_message(request, messages.ERROR,
            'Total number of weeks incorrect.  Total number of weeks should be: ' + str(c_totalweeks) +'.')
        success = False

    return success