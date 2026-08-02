# === Stage 32: Добавь журнал действий пользователя ===
# Project: EnergyLog
import datetime

class ActionLog:
    def __init__(self):
        self.actions = []
    
    def add_action(self, action_type, details, timestamp=None):
        if timestamp is None:
            timestamp = datetime.datetime.now()
        entry = {
            'timestamp': timestamp,
            'type': action_type,
            'details': details
        }
        self.actions.append(entry)
        return len(self.actions)
    
    def get_recent_actions(self, count=5):
        if not self.actions:
            return []
        recent = sorted(self.actions, key=lambda x: x['timestamp'], reverse=True)[:count]
        return recent
    
    def clear_log(self):
        self.actions.clear()
