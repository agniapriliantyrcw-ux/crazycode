# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: EnergyLog
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="EnergyLog CLI")
    sub = parser.add_subparsers(dest="command")

    p_log = sub.add_parser("log", help="Записать задачу")
    p_log.add_argument("--factor", type=str, help="Фактор")
    p_log.add_argument("--task", type=str, help="Задача")
    p_log.add_argument("--output", type=str, help="Файл вывода")

    p_report = sub.add_parser("report", help="Показать сводку")
    p_report.add_argument("--period", type=str, default="today", help="Период")

    p_reset = sub.add_parser("reset", help="Сбросить данные")
    args = parser.parse_args()

    if args.command == "log":
        print(f"[LOG] Фактор: {args.factor}, Задача: {args.task}")
        if args.output:
            with open(args.output, "a") as f:
                f.write(f"{args.factor}|{args.task}\n")
    elif args.command == "report":
        print(f"[REPORT] Период: {args.period}")
    elif args.command == "reset":
        print("[RESET] Данные сброшены")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
