# === Stage 20: Добавь восстановление записей из архива ===
# Project: EnergyLog
def load_archive(filepath):
    """Загружает записи из текстового архива в структуру EnergyLog."""
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|||')
            if len(parts) >= 6:
                record = {
                    'date': parts[0],
                    'period': parts[1],
                    'factor': parts[2],
                    'task': parts[3],
                    'output': int(float(parts[4])),
                    'note': parts[5].strip() if len(parts) > 6 else '',
                }
                records.append(record)
    return records
