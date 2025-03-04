def calculate_age():
    try:
        current_year = 2025
        birth_year = int(input("Enter your birth year: "))
        if birth_year > current_year:
            raise ValueError("Birth year cannot be in the future!")
        age = current_year - birth_year
        print(f"Your age is: {age} years")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number for the year.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


calculate_age()