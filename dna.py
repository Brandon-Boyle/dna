from csv import reader, DictReader
from sys import argv, exit


def main():

    # Make sure that there are the correct number of command line arguments
    if len(argv) < 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Open the csv file and convert it to a dictionary
    with open(argv[1], "r") as CSVfile:
        reader = DictReader(CSVfile)
        data_list = list(reader)

    # Open the DNA sequences file and convert it to a list
    with open(argv[2], "r") as sequencefile:
        sequence = sequencefile.read()

    # For the STRs, find the longest number of repeats in the sequence
    largest_repeat = []

    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[i]
        largest_repeat.append(0)

    # Iterate through the sequence to find the STR
        for j in range(len(sequence)):
            STR_repeats = 0

            # If an STR match has been found, begin to count the number of times it repeats
            if sequence[j:(j + len(STR))] == STR:
                z = 0
                while sequence[(j + z):(j + z + len(STR))] == STR:
                    STR_repeats += 1
                    z += len(STR)
                # if we find a new maximum number of repeats, update the largest_repeat varible with the new max
                if STR_repeats > largest_repeat[i - 1]:
                    largest_repeat[i - 1] = STR_repeats

    # Compare the largest repeat with the database files to see if there is a match
    for i in range(len(data_list)):
        exact_matches = 0
        for j in range(1, len(reader.fieldnames)):

            if int(largest_repeat[j - 1]) == int(data_list[i][reader.fieldnames[j]]):
                exact_matches += 1
            if exact_matches == (len(reader.fieldnames) - 1):
                print(data_list[i]['name'])
                exit(0)

    print("No match")


main()