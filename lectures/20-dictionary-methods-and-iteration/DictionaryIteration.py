from pprint import pprint
from ExtractData import extract_data_to_dict

VG_DATAFILE = "video_game_clean.csv"
PLATFORM_IDX = 0


def get_all_games_of_console(data, console_name):
    """
    Given a dictionary of video game data, extracts all of the video games that were released for the desired console
    and returns their names as a list.

    :param data: A dictionary of games of the format {GAME_NAME: [GAME_DATA]}
    :param console_name: The name of a video game console
    :return: A list of video game names
    """
    games = []

    # To iterate through both keys and values, we use the items() dictionary method
    for key_value in data.items():
        # items() gives us a tuple of the form (KEY, VALUE), so we can unpack both in one line
        game_name, game_data = key_value

        # Keep the game's name if this game's console is the desired one
        if game_data[PLATFORM_IDX] == console_name:
            games.append(game_name)

    return games


def main():
    game_data = extract_data_to_dict(VG_DATAFILE)
    games = get_all_games_of_console(game_data, "NES")

    print(len(games))
    pprint(games[:5])


main()
