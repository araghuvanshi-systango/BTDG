import random

from faker import Faker

from utils.selector import get_random_bank, get_random_month, get_random_year



faker = Faker()


def generate_random_digit_number(n: int) -> int:
    """
    Will generate a random n digit number
    """
    return random.randint(10**(n-1), (10**n)-1)


def generate_random_merchent_transaction() -> str:
    """
    Generate a random merchant transaction record

    format: UPI/P2M/133588806630/<merchent_name>/<bank_name>
    """

    return f"UPI/P2M/{generate_random_digit_number(12)}/{faker.name()}/{get_random_bank()}"


def generate_random_bank_transfer_transaction() -> str:
    """
    Generate a random bank transfer transaction record

    format: UPI/P2A/134227431807/<receiver_name>/<bank_name>/UPI
    """

    return f"UPI/P2A/{generate_random_digit_number(12)}/{faker.name()}/{get_random_bank()}/UPI"


def generate_random_salary_transaction() -> str:
    """
    Generate a random bank transfer transaction record

    format: INB-BULK-UPLD/115100334778/SALARY/<month>/<year>/<month>
    """

    month = get_random_month()
    year = get_random_year(2020, 2022)
    return f"INB-BULK-UPLD/{generate_random_digit_number(12)}/SALARY/{month.upper()}/{year}/{month}"


def generate_random_mutual_fund_transaction() -> str:
    """
    Generate a random bank transfer transaction record

    format: NACH-DR- GROWW
    """

    return "NACH-DR- GROWW"
