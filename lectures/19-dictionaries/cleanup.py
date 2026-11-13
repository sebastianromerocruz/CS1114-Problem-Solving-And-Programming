from sys import argv

DATA_IDX, CLEAN_IDX = 1, 2


if __name__ =="__main__":
    try:
        with open(argv[DATA_IDX], 'r') as file, open(argv[CLEAN_IDX], 'w') as clean_file:
            for line in file:
                line = line.strip().replace('"', '')
                print(line, file=clean_file)
    except FileNotFoundError:
        print(f"ERROR: Could not find file '{argv[DATA_IDX]}'.")
