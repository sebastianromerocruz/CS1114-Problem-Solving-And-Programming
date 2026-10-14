from random import uniform

MIN_FAHRENHEIT = 0.0
MAX_FAHRENHEIT = 100.0


def print_temps(temp_fahr):
    celsius = (temp_fahr - 32) * 5 / 9
    kelvin = celsius + 273.15
    rankine = temp_fahr + 459.67

    print("TEMPERATURE EQUIVALENTS")
    print(f"- FAHRENHEIT:\t{temp_fahr:>10.2f}")
    print(f"- CELSIUS:\t{celsius:>10.2f}")
    print(f"- KELVIN:\t{kelvin:>10.2f}")
    print(f"- RANKINE:\t{rankine:>10.2f}")


random_temp = uniform(MIN_FAHRENHEIT, MAX_FAHRENHEIT)
print_temps(random_temp)
