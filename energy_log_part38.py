# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: EnergyLog
def test_edge_cases():
    assert EnergyLog("2024-01-01 07:00") is None
    assert EnergyLog("2024-02-29 23:59") is None
    assert EnergyLog("2024-02-30 23:59") is None
    assert EnergyLog("2024-13-01 07:00") is None
    assert EnergyLog("2024-01-01 25:00") is None
    assert EnergyLog("01/02/2024 07:00") is None
    assert EnergyLog("2024-01-01 07:00:00") is None
    assert EnergyLog("2024-01-01 07:00:00:00") is None
    assert EnergyLog("2024-01-01 07:00:00:00:00") is None

    log = EnergyLog("2024-01-01 07:00")
    assert log is not None
    assert log.day == 1
    assert log.month == 1
    assert log.year == 2024
    assert log.hour == 7
    assert log.minute == 0

    log = EnergyLog("2024-12-31 23:59")
    assert log.day == 31
    assert log.month == 12
    assert log.year == 2024
    assert log.hour == 23
    assert log.minute == 59
