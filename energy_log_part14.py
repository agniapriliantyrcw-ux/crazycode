# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: EnergyLog
def generate_summary(data):
    if not data: return "Данных нет."
    periods = [p for p in data.get("periods", [])]
    tasks = [t for t in data.get("tasks", [])]
    factors = {f["name"]: f["value"] for f in data.get("factors", [])}
    outputs = data.get("outputs", [])
    
    lines = []
    lines.append(f"Сводка за сегодня ({len(periods)} периодов):")
    
    if periods:
        avg_energy = sum(p.get("energy", 0) for p in periods) / len(periods)
        lines.append(f"- Средняя энергия: {avg_energy:.1f}")
        best_period = max(periods, key=lambda x: x.get("energy", 0))
        lines.append(f"- Лучший период: {best_period.get('name', 'неизвестно')}")
    
    if tasks:
        completed = len([t for t in tasks if t.get("status") == "done"])
        total = len(tasks)
        pct = (completed / total * 100) if total else 0
        lines.append(f"- Выполнено задач: {completed}/{total} ({pct:.0f}%)")
    
    if factors:
        lines.append("- Факторы:")
        for name, value in list(factors.items())[:3]:
            lines.append(f"  • {name}: {value}")
    
    if outputs:
        lines.append("Выводы:")
        for out in outputs[-5:]:
            lines.append(f"- {out.get('text', '')}")
    
    return "\n".join(lines)
