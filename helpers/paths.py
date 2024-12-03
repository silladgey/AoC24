from urllib.parse import urljoin
from enums.test_inputs import TEST_INPUTS

BASE_URL = "https://adventofcode.com/"

paths = {
    "day03": {
        "file": "day03/input.txt",
        "url": urljoin(BASE_URL, "/2024/day/3/input"),
        "test_input": TEST_INPUTS.TEST_INPUT_3,
    }
}
