# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: EnergyLog
import unittest
from energylog import Day, Period, Factor, Task, Outcome

class TestEnergyLog(unittest.TestCase):
    def test_day_with_period(self):
        day = Day("Monday")
        morning = Period("Morning", Factor(energy=8, focus=7), Task("Plan day"), Outcome(score=9))
        day.add_period(morning)
        self.assertEqual(len(day.periods), 1)
        self.assertEqual(day.periods[0].name, "Morning")

    def test_factor_default_values(self):
        f = Factor()
        self.assertEqual(f.energy, 5)
        self.assertEqual(f.focus, 5)

    def test_outcome_calculation(self):
        outcome = Outcome(score=10)
        self.assertEqual(outcome.grade, "A")

    def test_task_with_description(self):
        task = Task("Write report")
        self.assertEqual(task.name, "Write report")

    def test_day_total_score(self):
        day = Day("Tuesday")
        morning = Period("Morning", Factor(energy=6, focus=6), Task("Code"), Outcome(score=7))
        evening = Period("Evening", Factor(energy=4, focus=4), Task("Read"), Outcome(score=5))
        day.add_period(morning)
        day.add_period(evening)
        self.assertEqual(day.total_score, 12)

if __name__ == "__main__":
    unittest.main()
