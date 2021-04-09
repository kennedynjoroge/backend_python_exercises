class Budget:
    def __init__(self, name, deposits, withdrawals, balance):
        self._name = name
        self.deposit = deposits
        self.withdrawals = withdrawals
        self.balance = balance

    def deposit_funds(self, deposit_amt):
        self.deposit += deposit_amt
        self.balance += deposit_amt

    def withdrawal_funds(self, withdrawal_amt):
        if self.balance > withdrawal_amt:
            self.withdrawals += withdrawal_amt
            self.balance -= withdrawal_amt
            op_result_code = 1
            op_result_msg = "Withdrawal Successful"
        else:
            op_result_code = 0
            op_result_msg = f"Withdrawal failure. Available balance {self.balance} is less than withdrawal amount {withdrawal_amt}"
        return op_result_code, op_result_msg

    def show_balance(self):
        print(
            f"{self._name}  Deposit amount: {self.deposit}, Withdrawal amount: {self.withdrawals} , Current balance: {self.balance}")

    def transfer(self, amount, target_account):
        self.withdrawal_funds(amount)
        target_account.deposit_funds(amount)


# Instantiate object
food = Budget("Food",0, 0, 0)
food.show_balance()

clothing = Budget("Clothing",0, 0, 10000)
clothing.show_balance()

print("====DEPOSIT===")
food.deposit_funds(10000)
food.show_balance()

print("====WITHDRAW===")
result_code, result_msg = food.withdrawal_funds(5000)
if result_code == 0:
    print(f"Withdrawal result code: {result_code}, Message:  {result_msg}")
elif result_code == 1:
    print(f"Withdrawal successful")
    food.show_balance()

print("====TRANSFER===")
clothing.transfer(5000, food)
food.show_balance()
clothing.show_balance()