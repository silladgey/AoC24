from urllib.parse import urljoin
from enums.test_inputs import TEST_INPUTS

BASE_URL = "https://adventofcode.com/"

paths = {
    "day01": {
        "file": "day01/input.txt",
        "url": urljoin(BASE_URL, "/2024/day/1/input"),
        "test_input": TEST_INPUTS.TEST_INPUT_1,
    }
}
