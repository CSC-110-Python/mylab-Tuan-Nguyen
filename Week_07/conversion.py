def pounds_to_kg(weight_lbs):
    return weight_lbs * 0.453592


def feet_to_cm(height_ft):
    return height_ft * 30.48


def main():
    weight_lbs = float(input("Enter weight in pounds (lbs): "))
    height_ft = float(input("Enter height in feet (ft): "))
    weight_kg = pounds_to_kg(weight_lbs)
    height_cm = feet_to_cm(height_ft)
    print(f"Weight: {weight_kg} kg")
    print(f"Height: {height_cm} cm")


if __name__ == "__main__":
    main()
