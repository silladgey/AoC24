from helpers.request import read_input
from helpers.paths import paths


def check_input(input_str: str) -> bool:
    if input_str is None:
        raise ValueError("Input cannot be empty")

    lines = input_str.strip().split("\n")
    for line in lines:
        if len(line.split()) != 2:
            raise ValueError(
                "Each line should contain two integers separated by a space"
            )
        if not line.split()[0].isdigit() or not line.split()[1].isdigit():
            raise ValueError("Each integer should be a positive number")

    return True


def prepare_lists(input_str: str) -> tuple[list[int], list[int]]:
    try:
        check_input(input_str)
    except ValueError as e:
        print(e)
        return ([], [])
    except IndexError as e:
        print(e)
        return ([], [])

    lines = input_str.strip().split("\n")
    left_list = [int(line.split()[0]) for line in lines]
    right_list = [int(line.split()[1]) for line in lines]

    return left_list, right_list


def part_one(input_str: str) -> int:
    left_list, right_list = prepare_lists(input_str)

    left_list.sort()
    right_list.sort()

    total_distance = 0

    while len(left_list) > 0:
        min1 = min(left_list)
        min2 = min(right_list)
        dist = abs(min1 - min2)
        total_distance += dist

        left_list.pop(left_list.index(min1))
        right_list.pop(right_list.index(min2))

    return total_distance


def part_two(input_str: str) -> int:
    left_list, right_list = prepare_lists(input_str)

    total_similarity_score = 0

    occurrences = {}

    for left in left_list:
        if left not in occurrences:
            occurrences[left] = right_list.count(left)
        else:
            occurrences[left] += right_list.count(left)

    for key, value in occurrences.items():
        total_similarity_score += key * value

    return total_similarity_score


if __name__ == "__main__":
    location_ids = read_input(paths["day01"], testing=True)  # for testing
    # location_ids = read_input(paths["day01"], use_local=True) # for local input.txt file

    total_distance = part_one(location_ids)
    total_similarity_score = part_two(location_ids)
