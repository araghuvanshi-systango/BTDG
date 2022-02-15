# BTDG (Bank Transaction Data Generator)

---

Generate bank transaction data.

## General Info

Python version: `3.8.10`
Total no. of transaction category: 4 (`MERCHENT`, `BANK_TRANSFER`, `SALARY` and `MUTUAL_FUND`)  
Default rows for each category: 5000  
BANKS: `Axis Bank`, `Yes Bank`, `ICICI Bank`, `HDFC Bank`, `State Bank` and `Fedral Bank`

## Setup

- Create a virtual env
```commandline
>>> virtualenv venv
```
- Install requirements
```commandline
>>> pip install -r requirements.txt
```

## Generating Data

```commandline
>>> python data_gen.py
```

## Fomat for transaction

- MERCHANT: `UPI/P2M/<12_digit_number>/<merchent_name>/<bank_name>`
- BANK_TRANSFER: `UPI/P2A/<12_digit_number>/<receiver_name>/<bank_name>/UPI`
- SALARY: `INB-BULK-UPLD/<12_digit_number>/SALARY/<month>/<year>/<month>`
- MUTUAL_FUND: `NACH-DR- GROWW`
