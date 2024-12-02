from day02.solution import part_one as d2_p1, part_two as d2_p2
from helpers.paths import paths
from helpers.request import read_input


def day02_main():
    reports = read_input(paths["day02"])

    safe_report_count = d2_p1(reports)
    dampener_safe_report_count = d2_p2(reports)

    print("Safe reports:", safe_report_count)
    print("Safe reports with dampener:", dampener_safe_report_count)


if __name__ == "__main__":

    print("\n--- Day 2: Red-Nosed Reports ---")
    day02_main()
