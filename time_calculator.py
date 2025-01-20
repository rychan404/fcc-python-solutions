def add_time(start, duration):
    # Split start time into hours, mins, & period
    split = start.index(':')
    start_hours = ''
    start_mins = ''
    start_period = ''

    for i in range(len(start)):
        if start[i].isdigit():
            if i < split:
                start_hours += start[i]
            else:
                start_mins += start[i]
        elif start[i].isalpha():
            start_period += start[i]

    # Split duration time into hours & mins
    split = duration.index(':')
    duration_hours = ''
    duration_mins = ''

    for i in range(len(duration)):
        if duration[i].isdigit():
            if i < split:
                duration_hours += duration[i]
            else:
                duration_mins += duration[i]

    # Convert to times to integers
    start_hours = int(start_hours)
    start_mins = int(start_mins)
    duration_hours = int(duration_hours)
    duration_mins = int(duration_mins)

    # Add duration_hours to start_hours
    new_hours = start_hours + duration_hours
    
    # Calculate number of times to switch AM & PM
    period_switch = new_hours // 12

    # Calculate leading hours term
    new_hours %= 12
    
    new_period = ''

    # Check to see when to switch AM to PM (or vice versa)
    if period_switch % 2 == 0:
        new_period = start_period
    elif start_period == 'AM':
        new_period = 'PM'
    else:
        new_period = 'AM'

    # Add duration_mins to start_mins
    new_mins = start_mins + duration_mins

    # Merge new times together
    new_time = str(new_hours) + ":" + str(new_mins) + " " + str(new_period)

    # Tests
    print(start_hours)
    print(start_mins)
    print(start_period)
    print(duration_hours)
    print(duration_mins)

    return new_time

# Tests
print(add_time('3:00 PM', '3:10'))
print(add_time('11:50 AM', '3:10'))