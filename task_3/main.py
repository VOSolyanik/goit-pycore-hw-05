import sys
from collections import namedtuple, Counter

Log = namedtuple("Log", ["date", "time", "level", "message"])

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]

def load_logs(file_path: str) -> list[str]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
            logs = [log.strip() for log in logs if log.strip()]
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Error: {e}")
    
    return logs


def parse_log_line(line: str) -> list[Log]:
    parts = line.split(' ')
    if len(parts) < 4:
        raise Exception("Невірний формат логу")
    if parts[2] not in LOG_LEVELS:
        raise Exception("Невірний рівень логування")
    return Log(parts[0], parts[1], parts[2], " ".join(parts[3:]))


def filter_logs_by_level(logs: list[Log], level: str) -> list[Log]:
    return [log for log in logs if log.level == level.upper()]


def count_logs_by_level(logs: list[Log]) -> dict:
    return Counter([log.level for log in logs])


def display_log_counts(counts: dict) -> None:
    level_column_title = "Рівень логування"
    amount_column_title = "Кількість"
    # Display table only if there are any logs
    if not counts:
        return
    
    print(f"{level_column_title} | {amount_column_title}")
    print(f"{'-' * (len(level_column_title) + 1)}|{'-' * (len(amount_column_title) + 1)}")
    # Display log counts table body
    for level, count in counts.items():
        print(f"{level}{' ' * (len(level_column_title) - len(level))} | {count}")

    print("")
    

def display_logs_by_level(logs: list[Log], level: str) -> None:
    filtered_logs = filter_logs_by_level(logs, level)
    # Display logs only if there are any
    if not logs:
       return
    
    print(f"Деталі логів для рівня {level.upper()}:")

    for log in filtered_logs:
        print(f"{log.date} {log.time} - {log.message}")


def main():
    has_file_path = len(sys.argv) >= 2

    if not has_file_path:
        print("Використання скрипту: python main.py [file_path]")
        return
    
    file_path = sys.argv[1]
        
    try:
        logs = [parse_log_line(log) for log in load_logs(file_path)]
        display_log_counts(count_logs_by_level(logs))
    except Exception as e:
        print(e)
    
    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        if log_level.upper() in LOG_LEVELS:
            display_logs_by_level(logs, log_level)
        else:
            print("Невірний рівень логування")

if __name__ == "__main__":
    main()