# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: EnergyLog
TEMPLATES = {
    "work": ("Work", "Work session", "Focus", "Work", 80, 160),
    "break": ("Break", "Short break", "Relax", "Rest", 10, 30),
    "deep": ("Deep Work", "Deep focus session", "Focus", "Work", 120, 240),
    "chill": ("Chill", "Leisure time", "Relax", "Rest", 30, 120),
    "review": ("Daily Review", "End-of-day reflection", "Reflect", "Work", 15, 45),
}

def apply_template(template_name, record):
    if template_name not in TEMPLATES:
        print(f"Unknown template: {template_name}")
        return
    name, title, energy, factor, duration_min, duration_max = TEMPLATES[template_name]
    record["name"] = record.get("name", name)
    record["title"] = record.get("title", title)
    record["energy"] = record.get("energy", energy)
    record["factor"] = record.get("factor", factor)
    record["duration_min"] = record.get("duration_min", duration_min)
    record["duration_max"] = record.get("duration_max", duration_max)
    return record
