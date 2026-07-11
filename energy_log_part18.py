# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: EnergyLog
def add_tag(self, tag: str) -> None:
    if not self._tags:
        self._tags = []
    if tag not in self._tags:
        self._tags.append(tag)

def remove_tag(self, tag: str) -> bool:
    return self._tags.remove(tag) if tag in self._tags else False

@property
def tags(self):
    return list(self._tags or [])

@tags.setter
def tags(self, value):
    self._tags = value if isinstance(value, list) else [value]
