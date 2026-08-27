# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: EnergyLog
def suggest_next_action(log, factors, tasks, outputs, day_periods):
    """Generate a short recommendation based on current log state."""
    if not log:
        return "Start by creating your first day period."
    
    active_tasks = [t for t in tasks if t['status'] == 'active']
    completed_outputs = [o for o in outputs if o['status'] == 'completed']
    
    if active_tasks and log:
        current_period = log[-1] if log else None
        if current_period.get('energy') < 3:
            return "You're low on energy. Consider a short break or switch to a lighter task."
        if not active_tasks:
            return "All tasks are done! Great job — consider adding new goals for tomorrow."
        if any(t.get('energy_cost', 0) > 5 for t in active_tasks):
            return "You have high-energy tasks ahead. Make sure you're well-rested."
        return f"Continue with active tasks: {[t['name'] for t in active_tasks]}"
    
    if log:
        return "Log your next day period to keep tracking your energy."
    
    return "Begin by logging today's first day period and set your initial energy level."
