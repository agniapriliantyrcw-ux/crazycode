# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: EnergyLog
def delete_record(record_id: int) -> bool:
    try:
        for record in records:
            if record['id'] == record_id:
                records.remove(record)
                return True
        print(f"Запись с ID {record_id} не найдена.")
        return False
    except Exception as e:
        print(f"Ошибка при удалении записи: {e}")
        return False

def get_missing_ids() -> list[int]:
    missing = []
    for record in records:
        if 'id' not in record or record['id'] is None:
            missing.append(record)
    return missing
