# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: EnergyLog
def print_project_metrics():
    if not project: return None
    total_energy = sum(day.energy for day in project)
    active_days = len([d for d in project if any(t.done for t in d.tasks)])
    completed_tasks = sum(len([t for t in d.tasks if t.done]) for d in project)
    total_tasks = sum(len(d.tasks) for d in project)
    avg_energy = (total_energy / active_days) if active_days else 0
    productivity = (completed_tasks / total_tasks * 100) if total_tasks else 0
    print(f"Total Energy: {total_energy} | Active Days: {active_days}/{len(project)}")
    print(f"Tasks Completed: {completed_tasks}/{total_tasks} ({productivity:.1f}%)")
    print(f"Avg Energy per Day: {avg_energy:.2f}")
