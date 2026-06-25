# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: EnergyLog
def main_menu():
    print("\n=== EnergyLog: Меню действий ===")
    print("1. Показать сводку дня (периоды, задачи)")
    print("2. Добавить новый период активности")
    print("3. Добавить задачу в текущий период")
    print("4. Вывести факторы влияния на энергию")
    print("5. Сохранить и завершить работу")
    print("0. Выход из программы")
    try:
        choice = input("Выберите действие (0-5): ").strip()
        if not choice.isdigit():
            print("Ошибка: введите число от 0 до 5.")
            return
        action = int(choice)
        if action == 1:
            for p in periods:
                print(f"\nПериод: {p['name']} ({p['start']}-{p['end']})")
                print(f"Факторы: {', '.join(p.get('factors', []))}")
                for t in p.get('tasks', []):
                    status = "✓" if t['done'] else "○"
                    print(f"  [{status}] {t['title']}")
        elif action == 2:
            name = input("Название периода: ").strip() or "Новый период"
            start = input("Время начала (HH:MM): ").strip() or now.strftime("%H:%M")
            end = input("Время окончания (HH:MM): ").strip() or f"{int(start.split(':')[0])+1}:00"
            periods.append({"name": name, "start": start, "end": end})
        elif action == 3 and periods[-1]:
            title = input("Название задачи: ").strip() or "Новая задача"
            done = input("Выполнено? (y/n): ").lower().startswith('y')
            if not periods[-1].get('tasks'):
                periods[-1]['tasks'] = []
            periods[-1]['tasks'].append({"title": title, "done": done})
        elif action == 4:
            print("\nФакторы энергии:")
            for i, f in enumerate(factors):
                print(f"{i+1}. {f}")
        elif action == 5:
            save_log()
            print("Данные сохранены. До свидания!")
            exit(0)
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
