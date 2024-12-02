import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_local(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")

    with open(file_path, encoding="utf-8") as f:
        return f.read()


def get_input(input_url: str) -> str:
    session_id = os.getenv("SESSION_ID")

    if not session_id:
        raise ValueError("SESSION_ID is not set in the environment variables")

    try:
        cookies = {"session": session_id}
        response = requests.get(input_url, cookies=cookies, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise SystemExit(e)

    return response.text


def read_input(
    path: dict, testing: bool = False, use_local: bool = False
) -> str | None:
    if testing:
        print("Using test input")
        test_input = path["test_input"].value
        print(test_input)
        return test_input

    if use_local:
        print("Using local input")
        try:
            return get_local(path["file"])
        except FileNotFoundError as e:
            print(e)
            return None

    return get_input(path["url"])
