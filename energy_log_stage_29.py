# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: EnergyLog
def build_app_config():
    return {
        "app_name": "EnergyLog",
        "language": "ru",
        "max_entries_per_day": 50,
        "energy_range": (1, 7),
        "productivity_range": (0.1, 1.0),
        "default_period": {
            "name": "Утро",
            "hours": [6, 9],
            "energy_factor": 0.85,
        },
        "display_date_format": "%d.%m.%Y",
    }
