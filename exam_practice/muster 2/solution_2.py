class NoMoney(Exception):
    pass

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.amount = 0

    def whitdraw(self, withdraw_amount):
        if withdraw_amount > self.amount:
            raise NoMoney("Not enough money")
        return self.amount - withdraw_amount


class CreditBankAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.credit_score = 1

    def whitdraw(self, withdraw_amount):
        try:
            withdraw = super().whitdraw(withdraw_amount)
            self.credit_score += 1
            return withdraw
        except NoMoney as error:
            self.credit_score -=1
            return  error


    def __add__(self, other):
        new_instance = CreditBankAccount(self.owner)
        new_instance.amount = self.amount + other.amount
        new_instance.credit_score = self.credit_score + other.credit_score

        return new_instance


def main():
    a1 = CreditBankAccount("Luca")
    a1.amount = 200

    a2 = CreditBankAccount("Daniel")
    a2.amount = 50

    a3 = a1 + a2
    print(f"{a3.owner},{a3.amount},{a3.credit_score}")

main()
