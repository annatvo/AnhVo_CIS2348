# Anh Vo
# 2037824
# 8.10

def palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()

    # Check if the text is the same when reversed
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    input_word = input('')
    if palindrome(input_word):
        print(f'{input_word} is a palindrome')
    else:
        print(f'{input_word} is not a palindrome')

if __name__ == '__main__':
    main()
