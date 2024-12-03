import re


def part_one(input_str: str) -> int:
    """
    Parses the input string to find all occurrences of the pattern "mul(x,y)",
    where x and y are integers, and returns the sum of all products of x and y.
    Args:
        input_str (str): The input string containing the patterns to be matched.
    Returns:
        int: The sum of all products of x and y found in the input string.
    """

    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(input_str)
    total = sum(int(x) * int(y) for x, y in matches)
    return total


def part_two(input_str: str):
    """
    Parses the input string to find all occurrences of the pattern "mul(x,y)",
    where x and y are integers, and returns the sum of all products of x and y,
    considering the enabling and disabling instructions.
    Args:
        input_str (str): The input string containing the patterns to be matched.
    Returns:
        int: The sum of all products of x and y found in the input string, considering the enabling and disabling instructions.
    """

    pattern = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    matches = pattern.findall(input_str)

    enabled = True
    total = 0

    for match in matches:
        if match[1] and match[2]:  # This is a mul(x,y) match
            if enabled:
                total += int(match[1]) * int(match[2])
        elif match[3]:  # This is a do() match
            enabled = True
        elif match[4]:  # This is a don't() match
            enabled = False

    return total
