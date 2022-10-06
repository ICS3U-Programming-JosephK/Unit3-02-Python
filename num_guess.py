#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 04
# This program checks if a user's integer guess is correct

# imports constants since there are no constants in python
import constants


def main():
    # input, get the user's guess (inter only)
    guess = int(input("Guess a number (integer): "))

    # check if the user's guess matches my constant and output if statement is correct
    if guess == constants.NUMBER:
        print("Your guess is right!")

    # check if the user's guess does not match my constant and output if statement is correct
    if guess != constants.NUMBER:
        print("Your guess is wrong!")


if __name__ == "__main__":
    main()
