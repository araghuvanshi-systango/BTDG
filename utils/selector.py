import random

from utils.constants import BANKS, MONTHS


def get_random_bank() -> str:
    """
    Returns a random selected bank from BANK list
    """
    return random.choice(BANKS)


def get_random_month() -> str:
    """
    Select random month
    """
    return random.choice(MONTHS)


def get_random_year(start: int, end: int) -> int:
    """
    Select random month
    """
    return random.randint(start, end+1)
