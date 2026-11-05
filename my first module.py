

class BankAccount:
    """
    Represents the bank account of the user 
    
    """
    def __init__(self, account_holder: str, balance: float = 0): 
        """
        initialize the bank account

        """

        self.account_holder = account_holder
        self.balance = balance

    def  deposit (self, amount: float):
        """
        Deposits an amount of money in their bank account

        Args:
           amount (float): the amount of money to deposit.

        Returns: 
        float: new balance
        
        """

        self.balance += amount
        print (f"Added to the account {amount} ")
        print (f"The new balance of the account is {self.balance}")
        return self.balance

    def withdraw(self, amount: float): 
        """
        withdraw an amount of money mpla mpla mpla

        
        """
        if self.balance <amount:
            print (f"{self.account_holder.upper()} you have Insufficient balance")
            return None 
        self.balance -= amount
        print(f"Withdrawn amount {amount} ")
        print (f" New balance is {self.balance}")

    def display_balance(self):
        print (f"{self.account_holder.upper()} your current balance is {self.balance}")
        return self.balance


rafail_account = BankAccount (account_holder='rafail balis')
rafail_account.deposit (1000)
rafail_account.withdraw (500)
rafail_account.display_balance()
    


# my_list = [2, 3, 5, 3, 7, 2, 5, 8, 5]
# cnt = 0
# print ("the numbers in the list are: ")
# for number in my_list:
#     print (f"the {number} in the list is in position {cnt}:")
#     cnt+=1

my_list = [2, 3, 5, 3, 7, 2, 5, 8, 5]
for cnt, number in enumerate (my_list):
    print (f"the {number} in the list is in position {cnt}:")