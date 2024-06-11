def create_fruit_dict():
    fruit_dict = {"banana": 1, "peach": 2, "nectarine": 3, "kiwi": 1, "apple": 3}
    return fruit_dict

if __name__ == "__main__":
    result = create_fruit_dict()
    print(result)


def has_odd(x):
    # Check if the set is empty
    if not x:
        return False

    # Iterate through the set and check for odd numbers
    for num in x:
        if num % 2 != 0:
            return True

    return False


# Example usage
if __name__ == "__main__":
    print(has_odd({1, 2, 3}))  # return True
    print(has_odd({2, 4, 6}))  # return False
    print(has_odd(set()))  # return False