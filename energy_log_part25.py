# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: EnergyLog
def parse_date(date_str):
    """Parse date string in YYYY-MM-DD format, return tuple or raise ValueError."""
    if not isinstance(date_str, str) or len(date_str.split('-')) != 3:
        raise ValueError(f"Некорректная дата: '{date_str}' — формат должен быть YYYY-MM-DD")
    y, m, d = date_str.split('-')
    try:
        year, month, day = int(y), int(m), int(d)
    except ValueError:
        raise ValueError(f"Некорректные числовые значения в дате: '{date_str}'")
    if not (1 <= year <= 9999):
        raise ValueError(f"Год вне диапазона: {year}")
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29
    if not (1 <= month <= 12):
        raise ValueError(f"Месяц вне диапазона: {month}")
    if not (1 <= day <= days_in_month[month]):
        raise ValueError(f"День '{day}' не соответствует месяцу {month}")
    return year, month, day
