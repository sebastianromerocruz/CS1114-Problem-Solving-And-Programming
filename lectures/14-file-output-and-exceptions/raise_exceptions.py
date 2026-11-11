def get_letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError(f"{score} is not a valid score (0-100)")

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'


def main():
    scores = [95, 72.5, 140, 81, -3]

    for score in scores:
        try:
            letter = get_letter_grade(score)
        except ValueError as error:
            print(f"WARNING: {error}")
        else:
            print(f"{score} -> {letter}")


main()
