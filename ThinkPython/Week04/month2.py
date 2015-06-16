
def july(date):
    """Given an integer DATE for a date in the month of July, print
    which day of the week it falls on. In 2015, July starts on a Wednesday.
    """
    # in 2015, July 1st fell on a Wednesday (day=3)
    first_day = 4
    day = ((date + first_day) % 7)
    if day == 0:
        print "Friday"
    elif day == 1:
        print "Saturday"
    elif day == 2:
        print "Sunday"
    elif day == 3:
        print "Monday"
    elif day == 4:
        print "Tuesday"
    if day == 5:
        print "Wednesday"
    elif day == 6:
        print "Thursday"

def myfun():
    print 'here is my function!'
    
myfun()