
def heating_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    elif actual_temp == desired_temp:
        print("Standby")

def convert_temp(temp_celsius, target_unit):
    if target_unit == "C":
        print(temp_celsius)
    elif target_unit == "F":
        print(temp_celsius * 1.8 + 32)
    elif target_unit == "K":
        print(temp_celsius + 273.15)


actual_temp = int(input("Please enter the current temperature: "))
desired_temp = int(input("Please enter your desired temperature: "))
temp_celsuis = desired_temp
target_unit = input("Please enter your target unit C, F, or K: ")

heating_cooling(actual_temp, desired_temp)
convert_temp(temp_celsuis, target_unit)

