# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: EnergyLog
import json, datetime as dt
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    energy_factor: float  # 0.1 - 1.0
    status: str = "pending"
    
def load_demo_data() -> dict[str, any]:
    tasks = [Task(1, "Собрать код", 0.8), Task(2, "Написать тесты", 0.6)]
    periods = {dt.time(9): {"factor": 0.7}, dt.time(14): {"factor": 0.5}}
    return {"tasks": tasks, "periods": periods}

def main():
    data = load_demo_data()
    print(f"Добро пожаловать в EnergyLog")
    for t in data["tasks"]:
        print(t)
