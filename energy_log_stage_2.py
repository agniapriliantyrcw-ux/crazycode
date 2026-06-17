# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: EnergyLog
class EnergyModel:
    def __init__(self):
        self.periods = []
        self.factors = {}
        self.tasks = []
        self.outputs = []

    def validate_period(self, name: str, start: int, end: int) -> bool:
        if not name or not (1 <= start < end <= 24):
            return False
        for p in self.periods:
            if p['name'] == name:
                return False
        self.periods.append({'name': name, 'start': start, 'end': end})
        return True

    def validate_factor(self, period_name: str, factor_type: str, value: float) -> bool:
        if not all([period_name, factor_type]):
            return False
        for p in self.periods:
            if p['name'] == period_name and p['start'] <= 12 <= p['end']:
                key = f"{p['name']}_{factor_type}"
                if key in self.factors:
                    self.factors[key] += value
                else:
                    self.factors[key] = value
                return True
        return False

    def validate_task(self, period_name: str, task_desc: str) -> bool:
        if not all([period_name, task_desc]):
            return False
        for p in self.periods:
            if p['name'] == period_name and p['start'] <= 12 <= p['end']:
                key = f"{p['name']}_{task_desc}"
                if key not in [t.get('key') for t in self.tasks]:
                    self.tasks.append({'period': period_name, 'desc': task_desc})
                    return True
        return False

    def validate_output(self, timestamp: str, content: str) -> bool:
        if not all([timestamp, content]):
            return False
        for o in self.outputs:
            if o['timestamp'] == timestamp and o['content'] == content:
                return False
        self.outputs.append({'timestamp': timestamp, 'content': content})
        return True

    def get_summary(self) -> dict:
        summary = {'periods': len(self.periods), 'factors_count': len(self.factors), 'tasks_count': len(self.tasks)}
        total_energy = sum(f['value'] for f in self.factors.values()) if self.factors else 0
        summary['total_energy_score'] = round(total_energy, 2)
        return summary
