#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program show if it's leaf year or not


def main():
    user_input = int(input("Enter a number: "))
    print("")

    if user_input % 4 == 0:
        if user_input % 100 == 0:
            if user_input % 400 == 0:
                print("It is a leaf year")
            else:
                print("not a leaf year")
        else:
            print("It is a leaf year")
    else:
        print("not a leaf year")


if __name__ == "__main__":
    main()
