# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: EnergyLog
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags is not None:
            record_tags = set(record.get('tags', []))
            if not all(tag in record_tags for tag in tags):
                continue
        filtered.append(record)
    return filtered

if __name__ == "__main__":
    print("Все записи:", records[:3])
    print("\nЗадачи в статусе 'В процессе':")
    active = filter_records(status='in_progress')
    for r in active:
        print(f"  [{r['status']}] {r.get('category', '?')} - {r['title']} ({', '.join(r.get('tags', []))})")

    print("\nЗадачи из категории 'Работа':")
    work = filter_records(category='work')
    for r in work:
        print(f"  [{r['status']}] {r.get('category', '?')} - {r['title']} ({', '.join(r.get('tags', []))})")

    print("\nЗадачи с тегом 'urgent':")
    urgent = filter_records(tags=['urgent'])
    for r in urgent:
        print(f"  [{r['status']}] {r.get('category', '?')} - {r['title']} ({', '.join(r.get('tags', []))})")
