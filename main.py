from day01.solution import part_one as d1_p1, part_two as d1_p2
from helpers.paths import paths
from helpers.request import read_input


def day01_main():
    try:
        location_ids = read_input(paths["day01"])
    except ValueError as e:
        print(e)
        return

    total_distance = d1_p1(location_ids)
    total_similarity_score = d1_p2(location_ids)

    print("Total distance:", total_distance)
    print("Total similarity score:", total_similarity_score)


if __name__ == "__main__":
    print("--- Day 1: Historian Hysteria ---")
    day01_main()
