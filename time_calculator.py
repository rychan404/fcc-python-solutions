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
    
    # Tests
    print(start_hours)
    print(start_mins)
    print(start_period)
    print(duration_hours)
    print(duration_mins)

    new_time = start
    return new_time

# Tests
print(add_time('3:00 PM', '3:10'))