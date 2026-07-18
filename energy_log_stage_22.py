# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: EnergyLog
def check_overdue_reminders():
    """Проверяет просроченные напоминания и возвращает список."""
    overdue = []
    for reminder in reminders:
        if reminder["time"] <= datetime.now().strftime("%Y-%m-%d %H:%M"):
            overdue.append(reminder)
    return overdue

def print_overdue_reminders():
    """Выводит просроченные напоминания."""
    overdue = check_overdue_reminders()
    if overdue:
        for reminder in overdue:
            print(f"Просрочено: {reminder['text']} (было в {reminder['time']})")
