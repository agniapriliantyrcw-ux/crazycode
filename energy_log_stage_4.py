# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: EnergyLog
def edit_record(record_id: int, updates: dict) -> bool | None:
    if not isinstance(updates, dict):
        return False
    for key in list(updates.keys()):
        if key not in RECORD_KEYS:
            raise ValueError(f"Недопустимое поле для редактирования: {key}")
    existing = next((r for r in records if r['id'] == record_id), None)
    if not existing:
        return False
    new_record = dict(existing)
    new_record.update(updates)
    # Обновляем метку времени на текущую при изменении статуса или контента
    if 'status' in updates or any(k in updates for k in TASK_CONTENT_FIELDS):
        new_record['updated_at'] = datetime.now().isoformat()
    index = next(i for i, r in enumerate(records) if r['id'] == record_id)
    records[index] = new_record
    return True

RECORD_KEYS = {'id', 'period_id', 'type', 'status', 'energy_level', 'productivity_score', 'notes'}
TASK_CONTENT_FIELDS = {'task_description', 'outcome_summary', 'factor_notes'}
