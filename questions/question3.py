# -*- coding: utf-8 -*-
"""
Question 3 -- changePossibilities(amount,amount): Your quirky boss collects rare, old coins. They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given an amount of money and an array of coin denominations, computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢
"""

def change_possibilities(amount, denominations):
    """
        Given an amount of money and an array of coin denominations, computes the number of ways to make the amount of money with coins of the available denominations
    """

    return _calculate_change(denominations, len(denominations), amount)

def _calculate_change(denominations, sub_denom, amount):

    new_amount = amount - denominations[sub_denom-1]

    if amount < 0:
        return 0
    elif sub_denom <= 0 and amount > 0:
        return 0
    elif amount == 0:
        return 1

    return _calculate_change(denominations, sub_denom, new_amount) + _calculate_change(denominations, sub_denom -1, amount)

if __name__ == '__main__':
    print(change_possibilities(4, [1,2,3]))
    print("--------------------")
    print(change_possibilities(2, [1,2]))
