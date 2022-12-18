import os
import time


class MainMenu():
    def __init__(self, listFood, listDrink):
        self.listFood = listFood
        self.listDrink = listDrink

    def displayMainMenu(self):
        while True:
            os.system('cls')
            print("*" * 30 + "MAIN MENU" + "*" * 30 + "\n"
                  "\t(O) ORDER\n"
                  "\t(O) ORDER\n"
                  "\t(O) ORDER\n"
                  "\t(O) ORDER\n" +
                  "_" * 70)

            input_1 = str(input("Select your choice: ")).upper()
            if input_1 in ['O', 'R', 'P', 'E']:
                time.sleep(1)
                os.system('cls')
                if input_1 == 'O':
                    pass
