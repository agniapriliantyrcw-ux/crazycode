# === Stage 17: Добавь группировку записей по категориям ===
# Project: EnergyLog
class Category:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    @property
    def count(self):
        return len(self.records)

def categorize(records, categories=None):
    if categories is None:
        categories = ['Work', 'Rest', 'Social']
    cat_map = {c.name.lower(): c for c in categories}
    for r in records:
        key = getattr(r, 'category', r.get('category', '')) or 'Other'
        target = cat_map.get(key)
        if target is None:
            target_name = key
            target = Category(target_name)
            cat_map[key.lower()] = target
        target.add_record(r)
    return list(cat_map.values())
