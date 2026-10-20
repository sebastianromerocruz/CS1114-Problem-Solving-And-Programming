def get_celsius(fahrenheit_temp):
    celsius = (fahrenheit_temp - 32.0) * (5.0 / 9.0)

    return celsius


def display_temperatures(filepath):
    # STEP 1: Open the file
    temp_file = open(filepath, 'r')  # opening filepath in read mode ('r')

    # STEP 2: Skip the header
    temp_file.readline()

    # STEP 3: Extract data from file
    for line in temp_file:
        line = line.strip()                      # get rid of potential new lines
        comma_idx = line.find(',')               # find location of the separating comma
        city_name = line[:comma_idx]             # isolate the city name
        temperature = line[comma_idx + 1:]       # isolate the temperature
        temperature = float(temperature)         # cast temperature str into float
        celsius_temp = get_celsius(temperature)  # get celsius equivalent

        print(f"The temperature in {city_name} is {round(celsius_temp, 2)}°C.")

    # STEP 4: Close the file
    temp_file.close()


def main():
    display_temperatures("../data.csv")


main()
