# import turtle
# from Aufgabe_3.letters.alphabet import *
# from Aufgabe_3.move_turtle.move import *
# from Aufgabe_3.punctuation_signs.punctuation import *
#
# tur = turtle.Turtle()
#
#
#
# def writeTurtle():
#     while True:
#         options_to_print()
#         option = input("Enter your option for the program: ".strip())
#
#         if option == "1":
#             optionCharacter = input("Write a letter ").strip()
#             if optionCharacter in character:
#                 character[optionCharacter](tur)
#             else:
#                 continue
#
#         elif option == "2":
#             print("Your options are: \n"
#                   "Press W to move forward 10 pixels \n"
#                   "Press S to move backwards 10 pixles \n"
#                   "Press A to rotate left \n"
#                   "Press D to rotate right \n"
#                   "Press G to put pen down \n"
#                   "Press F to put pen up")
#             # print_turtle_commands()
#
#             f = open("Aufgabe_3/user_input.txt", "w")  # Save the user input into the text file
#
#
#
#         else:
#             tur.clear()
#             break
# # writeTurtle()
