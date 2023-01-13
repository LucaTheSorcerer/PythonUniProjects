"""
Aufgabe 1
"""
import csv


def ub1(subject):
    with open("text.txt") as csvfile:
        reader = csv.reader()