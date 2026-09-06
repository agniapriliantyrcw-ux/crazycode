# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: EnergyLog
import copy, sys, os

def dry_run_mode():
    """Возвращает True, если флаг --dry-run задан в sys.argv."""
    return "--dry-run" in sys.argv

def dry_run_snapshot(data, path=""):
    """Создаёт текстовый отчёт о планируемом изменении данных."""
    lines = ["=== Dry-Run Snapshot ===", f"Path: {path or 'root'}",
             f"Data: {copy.deepcopy(data)}", ""]
    return "\n".join(lines)
