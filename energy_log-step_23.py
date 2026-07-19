# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: EnergyLog
def print_table(headers, rows):
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths) and len(str(cell)) > col_widths[i]:
                col_widths[i] = len(str(cell))
    fmt = ' | '.join(f'{{:<{w}}}' for w in col_widths)
    lines = [fmt.format(*headers), '-' * (sum(col_widths) + 3 * (len(headers) - 1))]
    for row in rows:
        lines.append(fmt.format(*row))
    print('\n'.join(lines))
