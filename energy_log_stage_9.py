# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: EnergyLog
import json, sys, os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

def load_initial_data(json_string: str) -> Dict[str, Any]:
    """Загружает начальные данные из JSON-строки и валидирует структуру."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_keys = ['periods', 'factors', 'tasks']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")
            
            if isinstance(data[key], list):
                for item in data[key]:
                    if not isinstance(item, dict):
                        raise TypeError(f"Элемент списка '{key}' должен быть словарем")

        # Установка метки времени для всех задач по умолчанию, если её нет
        now = datetime.now()
        if 'tasks' in data:
            for task in data['tasks']:
                if 'scheduled_at' not in task and 'start_time' not in task:
                    task['scheduled_at'] = {
                        "date": now.strftime("%Y-%m-%d"),
                        "hour": 9, # Дефолтный старт в 9 утра
                        "minute": 0
                    }

        return data

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка валидации данных: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    initial_json = '''
{
    "periods": [
        {"id": 1, "name": "Утро", "start_hour": 8, "end_hour": 12},
        {"id": 2, "name": "День", "start_hour": 13, "end_hour": 17}
    ],
    "factors": [
        {"id": 101, "name": "Кофеин", "boost": 15},
        {"id": 102, "name": "Прогулка", "boost": 10}
    ],
    "tasks": [
        {"title": "Собрать план", "category": "Planning"},
        {"title": "Написать код", "category": "Coding"}
    ]
}'''

    loaded_data = load_initial_data(initial_json)
    print(f"Загружено периодов: {len(loaded_data['periods'])}")
    print(f"Загружено факторов: {len(loaded_data['factors'])}")
    print(f"Загружено задач: {len(loaded_data['tasks'])}")
