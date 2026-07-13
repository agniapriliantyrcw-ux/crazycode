# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: EnergyLog
def archive_records(records, cutoff_days=None):
    """Archive completed or old records from the energy log."""
    if not records:
        return None
    
    archived = []
    kept = []
    
    for record in records:
        status = record.get('status', 'active')
        created_at = record.get('created_at', '')
        
        is_completed = status in ('completed', 'done', 'finished')
        
        if cutoff_days and not is_completed:
            import datetime
            now = datetime.datetime.now()
            age_days = (now - datetime.datetime.fromisoformat(created_at)).days
            should_archive = age_days > cutoff_days
            if should_archive:
                archived.append(record)
            else:
                kept.append(record)
        elif is_completed:
            archived.append(record)
        else:
            kept.append(record)
    
    return {
        'archived': archived,
        'kept': kept
    }
