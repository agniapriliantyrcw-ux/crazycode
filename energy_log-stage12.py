# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: EnergyLog
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            print(f"Загружено {len(data)} записей из '{filepath}'")
            return data
        elif isinstance(data, dict):
            print("Файл содержит объект JSON. Ожидается список.")
            return []
        else:
            print("Неверный формат данных в файле.")
            return []
    except FileNotFoundError:
        print(f"Ошибка: файл '{filepath}' не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
