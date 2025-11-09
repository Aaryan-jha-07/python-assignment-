# Name: [Aaryan Jha]
# Date: November 5, 2025
# Project Title: Daily Calorie Tracker 

import datetime

def print_welcome():
    """
    Task 1: Prints the welcome message for the application.
    """
    print("------------------------------------------")
    print("  Welcome to the Daily Calorie Tracker!   ")
    print("------------------------------------------")
    print("This tool helps you log your meals and track your total daily calorie intake.")
    print("\nLet's get started!\n")

def get_meal_inputs():
    """
    Task 2: Asks user for the number of meals and then collects
    the name and calories for each meal.
    Includes basic error handling for numeric inputs.
    """
    meal_names = []
    meal_calories = []

    # Get number of meals with error handling
    while True:
        try:
            num_meals = int(input("How many meals would you like to log today? "))
            if num_meals > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("") # Adding a space

    # Loop to get details for each meal
    for i in range(num_meals):
        meal_name = input(f"Enter name for meal #{i + 1}: ")
        
        # Get calorie amount with error handling
        while True:
            try:
                calories = float(input(f"Enter calories for {meal_name}: "))
                if calories >= 0:
                    break
                else:
                    print("Calories must be a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for calories.")
        
        meal_names.append(meal_name)
        meal_calories.append(calories)
        print("") # Adding a space for readability

    return meal_names, meal_calories

def calculate_calories(meal_calories):
    """
    Task 3: Calculates the total and average calories from the list.
    """
    total_calories = sum(meal_calories)
    
    # Avoid division by zero if the list is empty (though our input logic prevents this)
    if len(meal_calories) > 0:
        average_calories = total_calories / len(meal_calories)
    else:
        average_calories = 0
    
    return total_calories, average_calories

def check_calorie_limit(total_calories):
    """
    Task 3 & 4: Asks for daily limit, compares it, and
    returns the limit and a status message.
    """
    # Get daily limit with error handling
    while True:
        try:
            daily_limit = float(input("What is your daily calorie limit? "))
            if daily_limit > 0:
                break
            else:
                print("Please enter a positive number for your limit.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("") # Adding a space

    # Task 4: Compare total to the limit and create a message
    if total_calories > daily_limit:
        status_message = f"Warning: You went {total_calories - daily_limit:.0f} calories over your limit of {daily_limit:.0f}."
        print("**************************************************")
        print(status_message)
        print("**************************************************")
    else:
        status_message = f"Success! You are {daily_limit - total_calories:.0f} calories under your limit of {daily_limit:.0f}."
        print("--------------------------------------------------")
        print(status_message)
        print("--------------------------------------------------")
    
    return daily_limit, status_message

def print_summary_report(meal_names, meal_calories, total_calories, average_calories):
    """
    Task 5: Prints a neatly formatted summary of all meals and totals.
    """
    print("\n--- Your Daily Calorie Report ---")
    print("\nMeal Name\t\tCalories")
    print("---------------------------------")
    
    for i in range(len(meal_names)):
        # Using \t and f-string alignment to make the table neat
        print(f"{meal_names[i]:<15}\t{meal_calories[i]:>8.0f}")
    print(f"{'Average:':<15}\t{average_calories:>8.2f}")
    print("\n")

def save_log_to_file(meal_names, meal_calories, total_calories, average_calories, daily_limit, status_message):
    """
    Task 6 (Bonus): Asks the user if they want to save the report to a file
    and writes the data to 'calorie_log.txt'.
    """
    while True:
        save_choice = input("Would you like to save this session to 'calorie_log.txt'? (yes/no): ").strip().lower()
        if save_choice in ['yes', 'y', 'no', 'n']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if save_choice == 'yes' or save_choice == 'y':
        # Get current time for the log
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open("calorie_log.txt", "w") as file:
                file.write("--- Calorie Tracker Log ---\n")
                file.write(f"Session Time: {timestamp}\n")
                file.write("---------------------------\n\n")
                
                file.write("Meal Details:\n")
                for i in range(len(meal_names)):
                    file.write(f"- {meal_names[i]}: {meal_calories[i]:.0f} calories\n")
                
                file.write("\nSummary:\n")
                file.write(f"Total Calories: {total_calories:.0f}\n")
                file.write(f"Average Calories: {average_calories:.2f}\n")
                file.write(f"Daily Limit: {daily_limit:.0f}\n")
                
                file.write("\nStatus:\n")
                file.write(f"{status_message}\n")
            
            print("\nSuccessfully saved report to 'calorie_log.txt'")
        except IOError as e:
            print(f"\nError: Could not save file. {e}")
    else:
        print("\nReport not saved.")

def main():
    """
    Main function to run the calorie tracker application.
    """
    print_welcome()
    
    # Tasks 2: Get inputs
    names, calories = get_meal_inputs()
    
    # Task 3: Calculate
    total, average = calculate_calories(calories)
    
    # Task 5: Print summary
    print_summary_report(names, calories, total, average)
    
    # Tasks 3 & 4: Check limit
    limit, status = check_calorie_limit(total)
    
    # Task 6 (Bonus): Save to file
    save_log_to_file(names, calories, total, average, limit, status)
    
    print("\nThank you for using the Calorie Tracker!")

# Standard Python practice to run the main function
if __name__ == "__main__":
    main()