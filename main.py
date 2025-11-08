from datetime import datetime

date_str = input("Введіть дату формату YYYY-MM-DD ")

def get_days_from_today(date_str):
    try:
        year = datetime.strptime(date_str, "%Y-%m-%d")
        now = datetime.today()
        days_difference = (now - year).days
        return days_difference
    except ValueError:
        return "Невірний формат дати, використовуйте YYYY-MM-DD"

print(get_days_from_today(date_str))

