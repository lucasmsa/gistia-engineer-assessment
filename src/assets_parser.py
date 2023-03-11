import pandas as pd
from config.constants import COLUMNS, DATASET_URL
from util.get_google_sheets_csv_url import get_google_sheets_csv_url

class AssetsParser():
    def __init__(self, csv_url: str):
        self.df = pd.read_csv(csv_url)

    def fetch_unique_buy_sell_pairs(self) -> int:
        """Returns the quantity of unique buy/sell pairs from the dataset
        """
        buy_sell = self.df[[COLUMNS['buy'], COLUMNS['sell']]]
        unique_buy_sell = buy_sell.value_counts(ascending=True).reset_index(name="Unique pairs")
        unique_buy_sell_quantity = len(unique_buy_sell.index)

        return unique_buy_sell_quantity

    def fetch_accounts_with_at_least_500_transactions(self) -> int:
        """Returns the quantity of accounts with at least 500 transactions
        """
        accounts = self.df[COLUMNS['owner']]
        accounts_transactions = accounts.value_counts(ascending=False).reset_index(name="Number of transactions")
        accounts_with_at_least_500_transactions = len(accounts_transactions[accounts_transactions['Number of transactions'] >= 500].index)

        return accounts_with_at_least_500_transactions

    def fetch_third_highest_average_transaction_account(self) -> str:
        """Returns the account with the third highest average transaction
        """
        accounts_spendings = self.df[[COLUMNS['value'], COLUMNS['owner']]]
        mean_accounts_spendings = accounts_spendings.groupby(COLUMNS['owner']).mean()
        sorted_mean_accounts_spendings = mean_accounts_spendings.sort_values(by=COLUMNS['value'], ascending=False)
        third_highest_average_transaction_account = sorted_mean_accounts_spendings.index[2]

        return third_highest_average_transaction_account


csv_url = get_google_sheets_csv_url(DATASET_URL)

asset_parser = AssetsParser(csv_url=csv_url)

unique_pairs = asset_parser.fetch_unique_buy_sell_pairs()
accounts_with_at_least_500_transactions = asset_parser.fetch_accounts_with_at_least_500_transactions()
third_highest_average_transaction_account = asset_parser.fetch_third_highest_average_transaction_account()

print(f"Unique pairs: {unique_pairs}")
print(f"Accounts with at least 500 transactions: {accounts_with_at_least_500_transactions}")
print(f"Third highest average transaction account: {third_highest_average_transaction_account}")