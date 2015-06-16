def july(date):
    """Given an integer DATE for a date in the month of July, print
    which day of the week it falls on.
    """
    # in 2015, July 1st fell on a Wednesday (day=3)
    first_day = 3
    # subtract one from date to make it zero-based like our other math
    date = date - 1
    # mod 7 will tell us which (zero-based) day of the week it falls on
    # then we print that out
    print_day((date + first_day) % 7)


def print_day(day):
    """Given an integer code DAY for a day of the week, print its corresponding name.

    DAY ranges from 0-6 (Sunday-Saturday). 
    """
    # If it's a string, convert it to an int (Postel's Law)
    # principle: do such conversions early on
    day = int(day)
    if day == 0:
        print "Sunday"
    elif day == 1:
        print "Monday"
    elif day == 2:
        print "Tuesday"
    elif day == 3:
        print "Wednesday"
    elif day == 4:
        print "Thursday"
    elif day == 5:
        print "Friday"
    elif day == 6:
        print "Saturday"
    else:
        # principle: if you get bad input, tell what it is
        print "Unrecognized day", day
