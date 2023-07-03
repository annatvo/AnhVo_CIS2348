#Anh Vo
#2037824
#6.22
import math

def cal(a1, b1, c1, a2, b2, c2):
    for x in range (-10, 11):
        for y in range (-10, 11):
            if a1*x + b1*y == c1 and a2*x + b2*y == c2:
                return x, y
    return None

def main():
    # Enter 1st equation
    a1 = int(input(''))
    b1 = int(input(''))
    c1 = int(input(''))

    # Enter 2nd equation
    a2 = int(input(''))
    b2 = int(input(''))
    c2 = int(input(''))

    result = cal(a1, b1, c1, a2, b2, c2)

    if result:
        print(result[0], result[1])
    else:
        print('No solution')

if __name__ == "__main__":
    main()
