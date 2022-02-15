import pandas as pd

from utils.constants import TARGETS, BANKS, GENERATE_ROW_COUNT
from utils.generators import (
    generate_random_merchent_transaction,
    generate_random_bank_transfer_transaction,
    generate_random_salary_transaction,
    generate_random_mutual_fund_transaction
)


def main():
    # Generating data
    data = []
    for target in TARGETS:
        print(f'Generating data for target: {target}')
        for i in range(GENERATE_ROW_COUNT):
            row_dict = {'target': target}
            if target == 'MERCHENT':
                transaction_text = generate_random_merchent_transaction()
            elif target == 'BANK_TRANSFER':
                transaction_text = generate_random_bank_transfer_transaction()
            elif target == 'SALARY':
                transaction_text = generate_random_salary_transaction()
            elif target == 'MUTUAL_FUND':
                transaction_text = generate_random_mutual_fund_transaction()
            row_dict['text'] = transaction_text
            data.append(row_dict)
    
    # Converting data to dataframe
    df = pd.DataFrame(data)

    # Shuffle the rows of dataframe
    df = df.sample(frac=1).reset_index(drop=True)

    # Writing into csv
    df.to_csv('bank_transaction_data.csv', index=False)


if __name__ == '__main__':
    main()