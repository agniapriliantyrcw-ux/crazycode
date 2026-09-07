# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: EnergyLog
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "inverse": "\033[7m",
    "hidden": "\033[8m",
    "fg_red": "\033[31m",
    "fg_green": "\033[32m",
    "fg_yellow": "\033[33m",
    "fg_blue": "\033[34m",
    "fg_magenta": "\033[35m",
    "fg_cyan": "\033[36m",
    "fg_white": "\033[37m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m",
}

def colorize(text, color_key, enable=True):
    if enable and color_key in ANSI:
        return f"{ANSI[color_key]}{text}{ANSI['reset']}"
    return text

def log_info(msg, enable=True): return colorize(msg, "fg_blue", enable)
def log_success(msg, enable=True): return colorize(msg, "fg_green", enable)
def log_warning(msg, enable=True): return colorize(msg, "fg_yellow", enable)
def log_error(msg, enable=True): return colorize(msg, "fg_red", enable)
def log_dim(msg, enable=True): return colorize(msg, "fg_dim", enable)
