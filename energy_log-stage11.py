# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: EnergyLog
import json, os

def save_to_file(data: dict) -> None:
    filename = "energylog.json"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Ошибка сохранения в {filename}: {e}")

def load_from_file() -> dict:
    filename = "energylog.json"
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Файл повреждён, создаётся новый.")
    return {"periods": [], "factors": {}, "tasks": []}

def init_storage():
    if not os.path.exists("energylog.json"):
        save_to_file({"periods": [], "factors": {}, "tasks": []})
