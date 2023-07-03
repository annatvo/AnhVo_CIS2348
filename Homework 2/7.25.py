#Anh Vo
#2037824
#7.25

def exact_change(input_val):
    num_dollars = input_val // 100
    input_val %= 100

    num_quarters = input_val // 25
    input_val %= 25

    num_dimes = input_val // 10
    input_val %= 10

    num_nickles = input_val // 5
    input_val %= 5

    num_pennies = input_val

    return num_dollars, num_quarters, num_dimes, num_nickles, num_pennies

def main():
    input_val = int(input(''))

    if input_val <= 0:
        print('no change')
    else:
        dollars, quarters, dimes, nickels, pennies = exact_change(input_val)
        if dollars > 0:
            if dollars == 1:
                print("1 dollar")
            else:
                print(dollars, "dollars")

        if quarters > 0:
            if quarters == 1:
                print("1 quarter")
            else:
                print(quarters, "quarters")

        if dimes > 0:
            if dimes == 1:
                print("1 dime")
            else:
                print(dimes, "dimes")

        if nickels > 0:
            if nickels == 1:
                print("1 nickel")
            else:
                print(nickels, "nickels")

        if pennies > 0:
            if pennies == 1:
                print("1 penny")
            else:
                print(pennies, "pennies")

if __name__ == "__main__":
    main()
