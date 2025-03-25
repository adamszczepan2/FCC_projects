def add_time(start, duration, day=''):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    period = ['AM', 'PM']
    days = 0

    # Rozdzielenie wartości start
    start_hours, start_minutes = map(int, start[:-3].split(':'))
    start_period = start[-2:].upper()

    # Rozdzielenie wartości duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Konwersja start_hours na 24-godzinny format
    if start_period == 'PM' and start_hours != 12:
        start_hours += 12
    if start_period == 'AM' and start_hours == 12:
        start_hours = 0

    # Dodanie czasu
    total_minutes = start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes
    new_hours, new_minutes = divmod(total_minutes, 60)
    days, new_hours = divmod(new_hours, 24)

    # Konwersja z powrotem na 12-godzinny format
    new_period = 'AM' if new_hours < 12 else 'PM'
    new_hours = new_hours if 1 <= new_hours <= 12 else (12 if new_hours % 12 == 0 else new_hours % 12)

    # Obsługa dnia tygodnia
    if day:
        day_index = (week.index(day.lower()) + days) % 7
        new_day = f", {week[day_index].capitalize()}"
    else:
        new_day = ""

    # Obsługa liczby dni
    if days == 0:
        new_days = ""
    elif days == 1:
        new_days = " (next day)"
    else:
        new_days = f" ({days} days later)"

    # Sformatowany wynik
    return f"{new_hours}:{new_minutes:02d} {new_period}{new_day}{new_days}"


# Testy
print(add_time('3:30 PM', '2:12', 'Monday'))  # 5:42 PM, Monday
print(add_time('11:55 AM', '3:12'))           # 3:07 PM
print(add_time('9:15 PM', '5:30'))            # 2:45 AM (next day)
print(add_time('11:40 AM', '0:25'))           # 12:05 PM
print(add_time('2:59 AM', '24:00'))           # 2:59 AM (next day)
print(add_time('11:59 PM', '24:01', 'Wednesday'))  # 12:00 AM, Friday (2 days later)