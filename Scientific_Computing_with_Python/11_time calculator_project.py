def add_time(start = '0:00', duration = '0:00', day = ''):
    
    week = ['monday' ,'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    period = ['AM', 'PM']
    days = 0

    start_hours = start[:start.find(':')]
    start_minutes = start[start.find(':') + 1 :start.find(' ')]
    start_period = start[start.find(' ') + 1:].upper() 

    duration_hours = duration[:duration.find(':')]
    duration_minutes = duration[duration.find(':') + 1:]

    # start value errors
    if not start_hours.isdigit() and start_minutes.isdigit():
        raise ValueError("Wrong time value. Please try again")
    if int(start_hours) > 12 or len(start_hours) > 2:
        raise ValueError("Wrong hour value. Please try again")
    if int(start_minutes) > 59 or len(start_minutes) > 2:
        raise ValueError("Wrong minute value. Please try again")
    if not start_period in (period):
        raise ValueError("Wrong period value. Please try again")
    # duration value errors
    if int(duration_minutes) > 59 or len(duration_minutes) > 2:
        raise ValueError("Wrong duration minute value. Please try again")

    # change to 24 hour format
    if start_period == 'PM' and start_hours != 12:
        start_hours = int(start_hours) + 12
    
    new_hours = int(start_hours) + int(duration_hours)
    new_minutes = int(start_minutes) + int(duration_minutes)
    
    # new minutest and new hours calculation
    while new_minutes > 59:
        new_minutes -= 60
        new_hours += 1
    
    while new_hours > 23:
        new_hours -= 24
        days += 1
    
    # AM/PM calculation
    if new_hours > 12:
        new_hours -= 12
        new_period = period[1]
    else:
        new_period = period[0]
    
    if new_hours == 12 and new_minutes > 0:
        new_period = period[1]
    if new_hours == 0:
        new_hours = 12
        new_period = period[0]

    if day:
        day_index = (week.index(day.lower()) + days) % 7
        new_day = f", {week[day_index].capitalize()}"
    else:
        new_day = ""

    if days == 0:
        new_days = ""
    elif days == 1:
        new_days = " (next day)"
    else:
        new_days = f" ({days} days later)"

    new_time = f"{str(new_hours)}:{new_minutes:02d} {new_period}{new_day}{new_days}"

    return new_time

new_time = add_time('11:43 PM', '24:20', 'tueSday')
print(new_time)

# tests

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)