# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: EnergyLog
def print_record(record):
    """Компактный вывод одной записи: дата, статус, энергия, задача."""
    if not record:
        return "Нет записей."
    entry = record.get("entries", [])
    for e in entry:
        date = e.get("date", "?")
        status = e.get("status", "")
        energy = str(e.get("energy", ""))
        task = e.get("task", "")
        if not status and not task:
            continue
        line = f"[{date}] {status or 'Пусто'} | Энергия: {energy} | {task}"
        print(line)

def run():
    data = load_data()
    print_record(data)

run()
