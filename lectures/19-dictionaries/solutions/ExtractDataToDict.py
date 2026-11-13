VG_DATAFILE = "video_game_clean.csv"
NAME_IDX, PLATFORM_IDX, YR_IDX, GENRE_IDX, PUB_IDX, DEV_IDX = 1, 2, 3, 4, 5, 15


def extract_data_to_dict(filepath):
    data = {}

    try:
        with open(filepath, 'r') as file:
            file.readline()

            for game_data in file:
                split_datum = game_data.split(',')

                key = split_datum[NAME_IDX]
                value = [
                    split_datum[PLATFORM_IDX],
                    split_datum[YR_IDX],
                    split_datum[GENRE_IDX],
                    split_datum[PUB_IDX],
                    split_datum[DEV_IDX]
                ]

                # Step 6: If this entry doesn't already exist in our dictionary, add it
                if key not in data:
                    data[key] = value
    except FileNotFoundError:
        print(f"ERROR: Could not open file '{filepath}'")

    # Step 7: Return our whole data dictionary
    return data


def main():
    data = extract_data_to_dict(VG_DATAFILE)
    print(len(data))
    print(data["Custom Robo"])
    print(data["Dishonored"], data["Dishonored"][-1] != "")


main()
