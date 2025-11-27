def generate_profile(age:int) -> str:
    """
    Defines the user's stage of life by age.

        Parameters:
            age (int): The age of the user.

        Returns:
            str: One of the values
                - "Child" for ages 0-12
                - "Teenager" for ages 13-19
                - "Adult" for age 20+
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"

def print_profile(profile:dict) -> None:
    """
    Prints a beautifully designed user profile.

        Parameters:
            profile (dict): A dictionary with user data.
                Expected keys:
                    - "full name" (str)
                    - "age" (int)
                    - "life stage" (str)
                    - "hobbies" (list[str])
    """
    print("--- \nProfile Summary:")
    print(f'Name: {profile["full name"]}')
    print(f'Age: {profile["age"]}')
    print(f'Life Stage: {profile["life stage"]}')
    count_hobby = len(profile["hobbies"])
    if count_hobby >= 1:
        print(f'Favorite Hobbies ({count_hobby}):')
        for hobby in profile["hobbies"]:
            print(f'- {hobby}')
    else:
        print("You didn't mention any hobbies.")
    print("---")


# -----------------------------
# The main program
# -----------------------------


user_name = input("Enter your full name: ") # Requesting a name


# We get the year of birth and age
while True:
    try:
        birth_year_str = input("Enter your birth year: ")
        birth_year = int(birth_year_str)
        current_age = 2025 - birth_year
        if 0 <= current_age <= 150:
            break
        elif current_age < 0:
            print("Age cannot be negative. Please enter the correct value.")
        else:
            print("You're too old. Please enter the correct value.")
    except ValueError:
        print("Incorrect input. Please enter the number.")


hobbies = []


# Getting a hobby
while True:
    hobby_input = input("Enter a favorite hobby or type \'stop\' to finish: ")
    if hobby_input.lower() == "stop":
        break
    else:
        hobbies.append(hobby_input)


# Defining a life stage
life_stage = generate_profile(current_age)

# Forming the user's request
user_profile = {
    "full name": user_name,
    "age": current_age,
    "life stage": life_stage,
    "hobbies": hobbies,
}

# Printing the profile
print_profile(user_profile)
