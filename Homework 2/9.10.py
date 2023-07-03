# Anh Vo
# 2037824
# 9.10

import csv
def read_csv_file(file_name):
    word_freq = {}

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            for word in row:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    return word_freq

def main():
    file_name = input("")

    word_freq = read_csv_file(file_name)

    for word, freq in word_freq.items():
        print(word, freq)


if __name__ == "__main__":
    main()
