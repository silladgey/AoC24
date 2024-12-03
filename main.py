from day03.solution import part_one as d3_p1, part_two as d3_p2
from helpers.paths import paths
from helpers.request import read_input


def day03_main():
    corrupted_memory = read_input(paths["day03"])

    uncorrupted_result = d3_p1(corrupted_memory)
    uncorrupted_result_conditional = d3_p2(corrupted_memory)

    print("Uncorrupted result:", uncorrupted_result)
    print("Uncorrupted result (conditional):", uncorrupted_result_conditional)


if __name__ == "__main__":

    print("\n--- Day 3: Mull It Over ---")
    day03_main()
