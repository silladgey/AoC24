from helpers.request import read_input
from helpers.paths import paths


def is_safe(report):
    differences = [int(report[i + 1]) - int(report[i]) for i in range(len(report) - 1)]

    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return all_increasing or all_decreasing


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True

    return False


def part_one(input_str: str) -> int:
    input_str = input_str.strip()
    reports = input_str.split("\n")
    levels = [line.split() for line in reports]

    safe_report_count = sum(1 for report in levels if is_safe(report))
    return safe_report_count


def part_two(input_str: str):
    input_str = input_str.strip()
    reports = input_str.split("\n")
    levels = [line.split() for line in reports]

    dampener_safe_report_count = sum(
        1 for report in levels if is_safe_with_dampener(report)
    )
    return dampener_safe_report_count


if __name__ == "__main__":
    reports = read_input(paths["day02"], testing=True)  # for testing
    # reports = read_input(paths["day02"], use_local=True) # for local input.txt file

    safe_report_count = part_one(reports)
    dampener_safe_report_count = print(part_two(reports))
