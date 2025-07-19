def add_time(start, duration, day=''):   
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    count_days = 0

    time_part, noon = start.split()
    hours, minutes = map(int, time_part.split(":"))

    if noon.upper() == 'PM' and hours != 12:
        hours += 12
    if noon.upper() == 'AM' and hours == 12:
        hours = 0

    dhours, dminutes = map(int, duration.split(":"))
    hours += dhours
    minutes += dminutes

    if minutes >= 60:
        hours += 1
        minutes -= 60

    count_days = hours // 24
    hours = hours % 24

    if hours == 0:
        display_hour = 12
        noon = "AM"
    elif hours < 12:
        display_hour = hours
        noon = "AM"
    elif hours == 12:
        display_hour = 12
        noon = "PM"
    else:
        display_hour = hours - 12
        noon = "PM"

    if minutes < 10:
        minutes = "0" + str(minutes)
    new_time = f"{display_hour}:{minutes} {noon}"

    if day:
        d = (days.index(day.title()) + count_days) % 7
        new_day = days[d]
        new_time += f", {new_day}"

    if count_days == 1:
        new_time += " (next day)"
    elif count_days > 1:
        new_time += f" ({count_days} days later)"

    return new_time
