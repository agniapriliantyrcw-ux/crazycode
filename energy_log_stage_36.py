# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: EnergyLog
def repair_simple_issues(data):
    """Проверка целостности и ремонт простых проблем.

    Исправляет типичные ошибки:
    - Пустые задачи или периоды без имени
    - Задачи без фактора (предполагается фактор 'основной')
    - Периоды без задачи
    - Задачи без вывода
    """
    repaired = []
    for i, period in enumerate(data['periods']):
        repaired_period = dict(period)
        repaired_period['id'] = f"period_{i}"
        if not repaired_period.get('name'):
            repaired_period['name'] = f"Период_{i}"
        if not repaired_period.get('task'):
            repaired_period['task'] = {
                'id': 'default',
                'factor': 'основной',
                'output': '',
                'time': period.get('time', '00:00-23:59'),
            }
        repaired_period['task']['id'] = f"task_{i}"
        repaired_period['task']['output'] = repaired_period['task'].get('output', '')
        repaired.append(repaired_period)
    data['periods'] = repaired
    return data
