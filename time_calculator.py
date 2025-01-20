def add_time(start, duration):
    # Split start time into hours & mins
    split = start.index(':')
    start_hours = ''
    start_mins = ''
    for i in range(len(start)):
        if start[i].isdigit():
            if i < split:
                start_hours += start[i]
            else:
                start_mins += start[i]



    # Tests
    print(start_hours)
    print(start_mins)

    new_time = start
    return new_time

# Tests
print(add_time('3:00 PM', '3:10'))