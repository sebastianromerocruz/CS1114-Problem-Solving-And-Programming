def get_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32.0) * (5.0 / 9.0)


def display_temperatures(filepath):
    with open(filepath, 'r') as temp_file:
        temp_file.readline()  # header

        for line in temp_file:
            pieces = line.strip().split(',')

            city_name = pieces[0]
            temperature = float(pieces[1])

            print(f"The temperature in {city_name} is {round(get_celsius(temperature), 2)}°C.")


display_temperatures("data.csv")
