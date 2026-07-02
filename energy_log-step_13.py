# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: EnergyLog
def search_entries(query, fields=None):
    if not query: return []
    q = query.lower()
    if fields is None: fields = ['period', 'factor', 'task', 'output']
    results = [e for e in entries if any(q in str(getattr(e, f, '')).lower() for f in fields)]
    return sorted(results, key=lambda x: x.get('timestamp', ''), reverse=True)
