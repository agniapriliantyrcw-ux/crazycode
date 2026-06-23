# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: EnergyLog
def sort_entries(entries, key='date'):
    if not entries: return []
    reverse = False
    if key == 'priority':
        def _sort(e): return -e.get('priority', 0)
    elif key == 'name':
        def _sort(e): return e.get('name', '').lower()
    else:
        def _sort(e): return e.get(key, '')
    return sorted(entries, key=_sort, reverse=reverse)
