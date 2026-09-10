# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: EnergyLog
import shutil
from datetime import datetime


def backup_data_file(data_file_path: str, backup_dir: str = "backups") -> str:
    """Создаёт резервную копию файла данных в директории backups с меткой времени."""
    backup_dir = f"{data_file_path[:0]}{backup_dir}"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(data_file_path)}")
    shutil.copy2(data_file_path, backup_path)
    return backup_path
