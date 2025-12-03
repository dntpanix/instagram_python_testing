import requests
from framework.logger import log_info, log_error


def logout(url:str):
    """Make logout"""
    response = requests.get(f"{url}/logout")
    if response.ok:
        log_info("User logout done")
    else:
        log_error(f"Can't logout, get: {response}")
