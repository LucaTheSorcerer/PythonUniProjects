# 1.
# a. Geben sei eine Textdatei mit dem Namen "text.txt" an, die in jeder Zeile den Namen des Schülers, das Fach und
# die jeweilige Note enthält, getrennt durch ein Komma ",", schreiben Sie eine Funktion namens "ub1", die:
# 	- einen Parameter namens "subject" erhält
# 	- aus der angegebenen CSV-Datei "text.txt" liest
# 	- nur die Zeilen behält, deren Fach mit dem Parameter "subject" übereinstimmt (0.5p)
# 	- den Durchschnitt aller Noten berechnet und das Ergebnis zurückgibt (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
from functools import reduce
def ub1(subject):
    with open("text.txt", 'r') as file:
        data = file.readlines()
        subjectColumn = list(map(lambda line: line.strip() ,map(lambda line: line.split(',')[3], data)))
        filterdListBySubject = list(filter(lambda line: line.split(',')[2] == subject, data))
        medie = reduce(lambda number, suma: int(suma) + int(number),subjectColumn) / len(subjectColumn)
        return filterdListBySubject, medie

def correct_test():
    filteredbySubject, average = ub1("Advanced programming")
    print(average)
    assert  average == 8.666666666666666
    assert  len(filteredbySubject) == 6

correct_test()

# def incorrect_test():
#     filteredbySubject, average = ub1("Advanced programming")
#     print(average)
#     assert  average == 2
#     assert  len(filteredbySubject) == 4
# incorrect_test()


print(ub1("Advanced programming"))



# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "BankAccount".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
# 	 - bei der Initialisierung die Instanzvariable "amount" auf 0 und die Instanzvariable "owner" auf einen
# 	   gegebenen Parameter setzt (0.5p)
# 	 - eine Methode namens "withdraw" haben, die:
# 	 	- einen einzelnen ganzzahligen Parameter bekommt
# 	 	- prüft, ob der Parameter größer oder gleich der Variablen "amount" ist (0.5pp)
# 	 	- die Differenz zwischen dem "amount" und dem gegebenen Parameter zurückgibt (0.5p)
# 	 	- eine benutzerdefinierte Ausnahme namens "NoMoney" wirft, wenn der Parameter größer als "amount" ist (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "CreditBankAccount", die von "BankAccount" erbt.
#  Die Klasse sollte folgendes können:
# 	- bei der Initialisierung setzt sie neben den Variablen von "BankAccount" auch eine Instanzvariable namens
#  	  "credit_score" auf 1 (0.25p)
# 	- Überschreiben der Methode "withdraw", um Folgendes zu tun:
# 		- Wiederverwendung der Methode "withdraw" aus der Basisklasse (0.25)
# 		- im Falle einer erfolgreichen Abhebung* wird das Ergebnis zurückgegeben und der "credit_score" um 1 erhöht (0.25p)
# 		- im Falle einer fehlgeschlagenen Abhebung* wird "credit_score" um 1 verringert. (0.25p)
#         *Abhebung = erfolgreiche Aufruf zum "withdraw" Methode der Basisklasse
# 	- Die Summe von zwei Instanzen von "CreditBankAccount" (account_a + account_b) führt zu einer neuen Instanz
# 	  die den Namen des Eigentümers des ersten Kontos sowie "account" und "credit_score" als Summen der jeweiligen
# 	  Variablen der beiden Instanzen (1p)

class NoMoney(Exception):
    pass

class BankAccount:
    def __init__(self, owner):
        self.amount = 0
        self.owner = owner

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.amount:
            raise NoMoney("Not enough money!")
        return self.amount - withdraw_amount


class CreditBankAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.credit_score = 1

    def withdraw(self, withdraw_amount):

        try:
            withdraw = super().withdraw(withdraw_amount)
            self.credit_score += 1
            return withdraw
        except NoMoney as error:
            self.credit_score -= 1
            return error


    def __add__(self, other):
        new_amount = self.amount + other.amount
        new_credit_score = self.credit_score + other.credit_score
        newCredBankAccount = CreditBankAccount(self.owner)
        newCredBankAccount.amount = new_amount
        newCredBankAccount.credit_score = new_credit_score
        
        return newCredBankAccount



# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(n):
    if n in (0, 1):
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b



def recursive(n):
    if n == 0 or n == 1:
        return n
    return recursive(n-1) + recursive(n-2)

if __name__ == "__main__":
    acc1 = BankAccount("Alex")
    acc1.amount = 500
    #print(acc1.withdraw(200))

    acc2 = CreditBankAccount("Luca")
    acc3 = CreditBankAccount("Tudor")
    acc3.amount = 300
    acc2.amount = 600
    #print(acc2.amount)
    print(acc2.withdraw(10000))

    acc4 = acc2 + acc3
    print(f"{acc4.owner}, {acc4.amount}, {acc4.credit_score}, {acc4.withdraw(500)}")

    print(recursive(5))