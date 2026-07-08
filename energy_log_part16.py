# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: EnergyLog
def monthly_stats(daily_records):
    """Calculate monthly statistics grouped by year-month."""
    from collections import defaultdict
    stats = {}
    for date, record in daily_records:
        key = (date.year, date.month)
        if key not in stats:
            stats[key] = {'days': 0, 'total_energy': 0.0, 'tasks_completed': 0}
        stats[key]['days'] += 1
        stats[key]['total_energy'] += record.get('energy', 0)
        tasks = record.get('tasks', [])
        stats[key]['tasks_completed'] += sum(1 for t in tasks if isinstance(t, dict))
    return stats
