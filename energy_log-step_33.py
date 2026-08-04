# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: EnergyLog
def undo_last(self):
        if self.history:
            entry = self.history.pop()
            return entry
        return None
