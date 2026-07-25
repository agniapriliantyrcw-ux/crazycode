# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: EnergyLog
def reset_demo_data():
    """Сбросить все демо-данные: периоды, факторы, задачи, выводы."""
    demo_periods = [
        {"title": "Утро", "start": "08:00", "end": "12:00", "energy": 7, "productivity": 5},
        {"title": "День", "start": "12:00", "end": "16:00", "energy": 4, "productivity": 3},
        {"title": "Вечер", "start": "16:00", "end": "20:00", "energy": 5, "productivity": 4},
    ]
    demo_factors = [
        {"name": "сон", "value": 8, "effect": "+1"},
        {"name": "кофе", "value": 3, "effect": "+2"},
        {"name": "прогулка", "value": 4, "effect": "+1.5"},
    ]
    demo_tasks = [
        {"title": "Сделать отчёт", "duration_min": 60},
        {"title": "Проверить почту", "duration_min": 15},
    ]
    demo_outcomes = [
        {"task": "Отчёт", "outcome": "Успешно"},
        {"task": "Почта", "outcome": "Пропущено важное письмо"},
    ]
    return {
        "periods": demo_periods,
        "factors": demo_factors,
        "tasks": demo_tasks,
        "outcomes": demo_outcomes,
    }

def clear_state():
    """Полный сброс: очистить все коллекции и вернуть начальные демо-данные."""
    state = {
        "periods": [],
        "factors": [],
        "tasks": [],
        "outcomes": [],
        "logs": [],
        "stats": {},
    }
    demo = reset_demo_data()
    state["periods"] = demo["periods"]
    state["factors"] = demo["factors"]
    state["tasks"] = demo["tasks"]
    state["outcomes"] = demo["outcomes"]
    return state
