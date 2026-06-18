# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: EnergyLog
class EnergyLog:
    def __init__(self):
        self.entries = []
    
    def add_period(self, name, start_time, energy_level=50):
        period = {"name": name, "start_time": start_time, "energy_level": energy_level}
        self.entries.append(period)
        return period
    
    def add_task(self, period_name, task_description, productivity_factor=1.0):
        for entry in reversed(self.entries):
            if entry["name"] == period_name:
                task = {"period": period_name, "description": task_description, "factor": productivity_factor}
                self.entries.append(task)
                return task
        raise ValueError(f"Period '{period_name}' not found")
    
    def add_outcome(self, task_desc, result_text):
        for entry in reversed(self.entries):
            if isinstance(entry, dict) and entry.get("description") == task_desc:
                outcome = {"task": task_desc, "result": result_text}
                self.entries.append(outcome)
                return outcome
        raise ValueError(f"Task '{task_desc}' not found for adding outcome")
