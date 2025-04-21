class AccountSystem:
    def get_account(self, account_id):
        return f"Account {account_id} retrieved"
    
    def update_balance(self, account_id, amount):
        return f"Account {account_id} balance updated by ${amount}"

class TransactionSystem:
    def log_transaction(self, account_id, amount, type):
        return f"Transaction logged: {type} ${amount} from account {account_id}"
    
    def verify_funds(self, account_id, amount):
        return f"Verified sufficient funds in account {account_id}"

class NotificationSystem:
    def send_email(self, customer, message):
        return f"Email sent to {customer}: {message}"
    
    def send_sms(self, phone, message):
        return f"SMS sent to {phone}: {message}"

class BankingFacade:
    def __init__(self, accounts, transactions, notifications):
        self.accounts = accounts
        self.transactions = transactions
        self.notifications = notifications
    
    def withdraw(self, account_id, amount, customer_email, phone):
        results = []
        results.append(self.accounts.get_account(account_id))
        results.append(self.transactions.verify_funds(account_id, amount))
        results.append(self.accounts.update_balance(account_id, -amount))
        results.append(self.transactions.log_transaction(account_id, amount, "withdrawal"))
        results.append(self.notifications.send_email(customer_email, f"${amount} withdrawn"))
        results.append(self.notifications.send_sms(phone, f"${amount} withdrawn"))
        return "\n".join(results)