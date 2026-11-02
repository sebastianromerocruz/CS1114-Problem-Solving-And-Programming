TITLE_IDX = 0
PLAY_TIME_IDX = 2


def get_list_average(numbers):
    if len(numbers) == 0:
        return 0.0

    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum / len(numbers)


with open("library.csv", 'r') as library_file:
    library_file.readline()  # header

    play_times = []
    for line in library_file:
        pieces = line.strip().split(',')
        print(f"{pieces[TITLE_IDX]}: {pieces[PLAY_TIME_IDX]} hours")
        play_times.append(float(pieces[PLAY_TIME_IDX]))

print(f"Average play time: {round(get_list_average(play_times), 2)} hours")
