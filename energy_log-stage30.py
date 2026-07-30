# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: EnergyLog
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.active_profile = None

    def add(self, name, energy_levels=None, factors=None):
        if not name or name in self.profiles:
            return False
        profiles = {"energy_levels": {1: 80, 2: 75, 3: 65}, "factors": []}
        if energy_levels is None and factors is None:
            profiles["name"] = name
        else:
            profiles["name"] = name
            for lvl, val in (energy_levels or {}).items():
                profiles["energy_levels"][lvl] = val
            if factors is not None:
                profiles["factors"] = factors
        self.profiles[name] = profiles
        return True

    def set_active(self, name):
        if name in self.profiles and self.profiles[name]["active"]:
            self.active_profile = name
            return True
        return False
