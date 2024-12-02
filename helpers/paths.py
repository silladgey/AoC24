from urllib.parse import urljoin
from enums.test_inputs import TEST_INPUTS

BASE_URL = "https://adventofcode.com/"

paths = {
    "day02": {
        "file": "day02/input.txt",
        "url": urljoin(BASE_URL, "/2024/day/2/input"),
        "test_input": TEST_INPUTS.TEST_INPUT_2,
    }
}
