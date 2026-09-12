# === Stage 45: Добавь восстановление из резервной копии ===
# Project: EnergyLog
def restore_from_backup():
    backup_path = input("Введите путь к резервному файлу: ").strip()
    if not backup_path:
        print("Путь не указан.")
        return False
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        print("Резервная копия успешно загружена.")
        return data
    except FileNotFoundError:
        print(f"Файл {backup_path} не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка: некорректный формат JSON.")
        return None
