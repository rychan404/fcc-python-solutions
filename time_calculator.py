def add_time(start, duration, start_day_of_week=''):
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

    # Add duration_mins to start_mins
    new_mins = start_mins + duration_mins
    new_hours = new_mins // 60
    new_mins %= 60

    # Add duration_hours to start_hours
    new_hours += start_hours + duration_hours
    
    # Calculate number of times to switch AM & PM
    period_switch = new_hours // 12

    # Calculate number of days later
    days_later = new_hours // 24

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

    # Convert leading mins term 0 to 00
    if new_mins == 0:
        new_mins = '00'

    # Convert leading hours term 0 to 12
    if new_hours == 0:
        new_hours = 12

    # List of days of the week
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # Convert start_day_of_week to lowercase
    start_day_of_week = start_day_of_week.lower()

    # Convert start_day_of_week to numerical index of days_of_week
    for i in range(len(days_of_week)):
        if start_day_of_week == days_of_week[i]:
            start_day_of_week = i

    # Merge new times together
    new_time = str(new_hours) + ":" + str(new_mins) + " " + str(new_period)

    if start_day_of_week != '':
        # Find index of day of the week that corresponds to the list
        new_day_of_week = (start_day_of_week + days_later) % 7

        # Change new_day_of_week to the actual day of the week
        new_day_of_week = days_of_week[new_day_of_week]

        # Capitalize first letter of day of the week
        new_day_of_week = new_day_of_week.capitalize()

        # Add day of the week
        if days_of_week != '':
            new_time += f', {new_day_of_week}'
        
    # Add number of days later
    if days_later > 1:
        new_time += f' ({days_later} days later)'
    elif days_later == 1:
        new_time += ' (next day)'

    # Tests
    print(start_hours)
    print(start_mins)
    print(start_period)
    print(duration_hours)
    print(duration_mins)

    return new_time

# Tests
print(add_time('3:00 PM', '3:10'))
print(add_time('11:50 AM', '48:10', 'Monday'))