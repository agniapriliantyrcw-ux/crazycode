# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: EnergyLog
import sys
from io import StringIO

def demo_energylog():
    """Quick manual testing block for EnergyLog."""
    print("=== EnergyLog Demo ===")
    
    # Import and run basic flow
    from energy_log.models.task import Task
    from energy_log.models.period import Period
    from energy_log.models.factor import Factor
    
    # Create a task
    task = Task(
        title="Write Python script",
        duration_minutes=60,
        difficulty="medium"
    )
    
    # Create a period
    period = Period(
        start_hour=9,
        end_hour=17,
        name="Work Day"
    )
    
    # Create factors
    factor_focus = Factor(name="Focus", value=0.8)
    factor_energy = Factor(name="Energy", value=0.6)
    
    # Test task creation
    print(f"\nTask: {task.title}")
    print(f"Duration: {task.duration_minutes} minutes")
    print(f"Difficulty: {task.difficulty}")
    
    # Test period creation
    print(f"\nPeriod: {period.name}")
    print(f"Time: {period.start_hour}:00 - {period.end_hour}:00")
    
    # Test factor creation
    for f in [factor_focus, factor_energy]:
        print(f"Factor: {f.name} = {f.value}")
    
    # Test period with task (if methods exist)
    try:
        result = period.evaluate(task, factors=[factor_focus])
        print(f"\nEvaluation: {result}")
    except Exception as e:
        print(f"\nEvaluation skipped: {e}")
    
    print("\n=== Demo Complete ===")

# Run demo on import or manually
if __name__ == "__main__":
    demo_energylog()
