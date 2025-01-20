def add_time(start, duration):
    # Split start time into hours & mins
    split = start.index(':')
    hours = ''
    mins = ''
    for i in range(len(start)):
        if start[i].isdigit():
            if i < split:
                hours += start[i]
            else:
                mins += start[i]

    # Tests
    print(hours)
    print(mins)

    new_time = start
    return new_time

# Tests
print(add_time('3:00 PM', '3:10'))