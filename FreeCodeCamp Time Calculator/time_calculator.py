def add_time(start, duration, starting_day=''):
    # A list with weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # I split the start into time and meridian
    starting_time, am_or_pm = start.split()
    # I split it again ang get hold of the hours and then minutes
    hours, minutes = starting_time.split(':')
    # I do the same with the time to be added, I split it and get hold of hours and minutes
    added_hours, added_minutes = duration.split(':')
    # I set my meridian value to the given one, and later I'll switch it in accordance.
    meridiem_new_time = am_or_pm

    # I calculate if the duration is more than 24 hours, and if so, how many days
    added_days = round(int(added_hours) / 24)
    added_days_not_rounded = round(int(added_hours) / 24, 2)
    if added_days_not_rounded > added_days > 1:
        added_days += 1

    # Here I calculate duration in hours, if more than 24 hours added
    # -> notice I use modulous for it (%), basically if it's more than 24 hours, it counts
    # from 0 again, as in the clock.
    added_hours_after_days = int(added_hours) % 24
    if added_days >= 1:
        added_hours = added_hours_after_days

    # I turn the hours to integers and add them
    result_add_hours = int(hours) + int(added_hours)
    # I turn the minutes to integers and add them
    result_add_minutes = int(minutes) + int(added_minutes)
    # I make sure the addition of minutes going over 60 is corrected
    if result_add_minutes >= 60:
        result_add_hours += 1
        result_add_minutes -= 60
        if added_days == 1:
            added_days += 1

    next_day_string = '(next day)'

    # This changes the meridiem in acordance
    if result_add_hours >= 12 or result_add_hours == 11 and result_add_minutes >= 60:
        result_add_hours -= 12
        if result_add_hours == 0:
            result_add_hours = 12
        if am_or_pm == 'PM':
            if added_days < 1:
                meridiem_new_time = 'AM'
            else:
                meridiem_new_time = 'AM'
        elif am_or_pm == 'AM':
            meridiem_new_time = 'PM'

    # This is to make it look better if minutes below 10 (e.g. "4:04")
    if result_add_minutes < 10:
        result_add_minutes = f'0{result_add_minutes}'

    # -----------------   FIGURING OUT THE ENDING WEEK DAY ---------------------------------
    if starting_day != '':
        index = weekdays.index(starting_day.capitalize())
        index += added_days
        if index > 7:
            index = index % 7
        result_weekday = weekdays[index]
    else:
        result_weekday = ''

    # DEFINING THE NEW TIME STRING TO BE RETURNED ------------------------------------
    new_time = ''
    # --- >>> LESS than 24 hours added
    if added_days < 1 and result_weekday != '':
        new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time}, {result_weekday}'

    elif added_days < 1:
        if meridiem_new_time == 'AM' and am_or_pm == 'PM':
            new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time} {next_day_string}'
        else:
            new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time}'

    # --- >>> MORE than 24 hours added
    elif added_days == 1:
        if result_weekday != '':
            new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time}, {result_weekday} {next_day_string}'
        else:
            new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time} {next_day_string}'

    # If more than 24 hours are added AND a starting day was given:
    elif added_days > 1 and result_weekday != '':
        new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time}, ' \
                   f'{result_weekday} ({added_days} days ' \
                   f'later)'

    # If more than 24 hours are added BUT a starting day was NOT given:
    elif added_days > 1 and result_weekday == '':
        new_time = f'{result_add_hours}:{result_add_minutes} {meridiem_new_time} ' \
                   f'{result_weekday}({added_days} days ' \
                   f'later)'

    return new_time
