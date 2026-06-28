# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: EnergyLog
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "periods": periods,
        "factors": factors,
        "tasks": tasks,
        "outputs": outputs,
        "meta": {"version": 1.0}
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
