from pprint import pprint

PREFERENCES = "preferences.csv"


def extract_preferences(filepath):
    """
    Extracts user preferences from a CSV file. Uses zeroth element in each line as key, and first element as value.
    Assumes all lines are valid entries. If file not found, returns an empty dictionary.

    :param filepath: Address of CSV file in string form
    :return: A dictionary of preferences
    """
    pass


def main():
    preferences = extract_preferences(filepath=PREFERENCES)
    pprint(preferences)


main()
