# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: EnergyLog
def weekly_stats(daily_records):
    """Calculate weekly statistics grouped by date."""
    from collections import defaultdict, Counter
    
    if not daily_records:
        return {}
    
    stats = defaultdict(lambda: {
        'total_energy': 0,
        'tasks_done': 0,
        'total_time_min': 0,
        'periods_active': set()
    })
    
    for date_str, record in daily_records.items():
        energy = record.get('energy', 0)
        tasks = record.get('tasks', [])
        time_min = record.get('time_minutes', 0)
        
        stats[date_str]['total_energy'] += energy
        stats[date_str]['total_time_min'] += time_min
        
        for task in tasks:
            if task.get('status') == 'done':
                stats[date_str]['tasks_done'] += 1
            
            for period in task.get('periods', []):
                stats[date_str]['periods_active'].add(period)
    
    return dict(stats)
