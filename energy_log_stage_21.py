# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: EnergyLog
class Reminder:
    def __init__(self, title, date=None):
        self.title = title
        self.date = date if date else datetime.now().date()

    def is_due(self):
        return self.date <= datetime.now().date()

    def __str__(self):
        status = "due" if self.is_due() else "upcoming"
        return f"[{status}] {self.title} ({self.date})"


def add_reminders(reminders, title="Напоминания", date=None):
    reminders.append(Reminder(title, date))


if __name__ == "__main__":
    reminders = []
    today = datetime.now().date()
    tomorrow = (today + timedelta(days=1)).isoformat()

    add_reminders(reminders, "Выпить воду", today)
    add_reminders(reminders, "Сделать зарядку", tomorrow)
    add_reminders(reminders, "Купить молоко")

    for r in reminders:
        print(r)
