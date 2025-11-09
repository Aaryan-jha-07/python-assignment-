
"""
File: gradebook.py
Name: [Aaryan Jha]
Date: [8 nov 2025]
Title: GradeBook Analyzer
"""

# Import csv module for Task 2
import csv
import sys

# --- Task 2: Data Entry Functions ---

def get_manual_marks():
    """
    
    Task 2a: Allows manual entry of student names and marks.
    Loops until the user types 'done'.
    Returns a dictionary of marks: {"Name": score}
    """
    print("\n--- Manual Mark Entry ---")
    print("Enter student name and mark. Type 'done' as the name to finish.")
    
    # Store data in a dictionary
    marks_dict = {}
    while True:
        name = input("Enter student name: ")
        if name.lower() == 'done':
            break
        
        try:
            # Get and validate the score
            score_str = input(f"Enter mark for {name}: ")
            score = int(score_str)
            
            if 0 <= score <= 100:
                marks_dict[name] = score
            else:
                print("Invalid mark. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Mark must be a number. Please try again.")
            
    print(f"Data entry complete. {len(marks_dict)} students recorded.")
    return marks_dict

def get_csv_marks():
    """
    
    Task 2b: Loads marks from a specified CSV file.
    Assumes CSV format: Name,Mark (with a header row)
    Returns a dictionary of marks: {"Name": score}
    """
    print("\n--- CSV File Import ---")
    filename = input("Enter the CSV file name (e.g., marks.csv): ")
    
    # Store data in a dictionary
    marks_dict = {}
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            # Skip the header row
            header = next(reader)
            print(f"Reading CSV with headers: {', '.join(header)}")
            
            count = 0
            for row in reader:
                try:
                    name = row[0]
                    score = int(row[1])
                    if 0 <= score <= 100:
                        marks_dict[name] = score
                        count += 1
                    else:
                        print(f"Warning: Invalid score {score} for {name}. Skipping.")
                except (ValueError, IndexError):
                    print(f"Warning: Skipping invalid row: {row}")
                    
            print(f"Successfully loaded {count} students from {filename}.")
            return marks_dict
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# -[span_0](start_span)-- Task 3: Statistical Analysis Functions ---[span_0](end_span)

def calculate_average(marks_dict):
    """Calculates the average (mean) score."""
    if not marks_dict:
        return 0
    scores = marks_dict.values()
    return sum(scores) / len(scores)

def calculate_median(marks_dict):
    """Calculates the median score."""
    if not marks_dict:
        return 0
    
    sorted_scores = sorted(marks_dict.values())
    n = len(sorted_scores)
    
    if n % 2 == 1:
        # Odd number of students
        median = sorted_scores[n // 2]
    else:
        # Even number of students
        mid1 = sorted_scores[n // 2 - 1]
        mid2 = sorted_scores[n // 2]
        median = (mid1 + mid2) / 2
    return median

def find_max_score(marks_dict):
    """Finds the highest score and the student who earned it."""
    if not marks_dict:
        return "N/A", 0
    # Use max() with a key to find the item with the highest value
    top_student = max(marks_dict, key=marks_dict.get)
    max_score = marks_dict[top_student]
    return top_student, max_score

def find_min_score(marks_dict):
    """Finds the lowest score and the student who earned it."""
    if not marks_dict:
        return "N/A", 0
    bottom_student = min(marks_dict, key=marks_dict.get)
    min_score = marks_dict[bottom_student]
    return bottom_student, min_score

# -[span_1](start_span)-- Task 4: Grade Assignment and Distribution ---[span_1](end_span)

def assign_grades(marks_dict):
    """
    Assigns letter grades based on marks and counts the distribution.
    Returns two dictionaries:
    1. student_grades: {"Name": "Grade"}
    2. grade_distribution: {"Grade": count}
    """
    student_grades = {}
    # 
    grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    # Grade scale: A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60
    for student, score in marks_dict.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
            
        student_grades[student] = grade
        grade_distribution[grade] += 1
        
    return student_grades, grade_distribution

# -[span_2](start_span)-- Task 5: Pass/Fail Filter ---[span_2](end_span)

def filter_pass_fail(marks_dict):
    """
    Uses list comprehensions to filter passed and failed students.
    Prints the lists as required by the task.
    """
    print("\n--- Pass/Fail Analysis ---")
    
    # Use list comprehension, Pass condition: score >= 40
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    
    print(f"Total Passed ({len(passed_students)}): {', '.join(passed_students) or 'None'}")
    print(f"Total Failed ({len(failed_students)}): {', '.join(failed_students) or 'None'}")
    # (End of task 5 deliverable)

# -[span_3](start_span)-- Task 6: Results Table ---[span_3](end_span)

def print_results_table(marks_dict, grades_dict):
    """
    Prints a formatted table of student results.
    Uses f-strings and tabs (\t) for formatting.
    """
    print("\n--- Full Grade Report ---")
    # Print Header
    print(f"{'Name':<20}\t{'Mark':<5}\t{'Grade':<5}")
    print("-" * 35)
    
    # Print student rows
    for name, mark in marks_dict.items():
        grade = grades_dict.get(name, 'N/A')
        print(f"{name:<20}\t{mark:<5}\t{grade:<5}")
        
# -[span_4](start_span)-- Bonus: Save to CSV ---[span_4](end_span)

def save_results_to_csv(marks_dict, grades_dict):
    """
    (Bonus Task) Saves the final grade table to a new CSV file.
    """
    filename = input("\nEnter filename to save results (e.g., results.csv): ")
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(['Name', 'Mark', 'Grade'])
            # Write data
            for name, mark in marks_dict.items():
                grade = grades_dict.get(name, 'N/A')
                writer.writerow([name, mark, grade])
        print(f"Successfully saved results to {filename}")
    except Exception as e:
        print(f"Error: Could not save file. {e}")

# --- Main Program Logic ---

def process_analysis(marks_data):
    """
    Runs all analysis tasks (3, 4, 5, 6) on the provided marks data.
    """
    if not marks_data:
        print("No student data to analyze.")
        return

    # --- Task 3: Statistical Analysis ---
    print("\n" + "=" * 35)
    print("      STATISTICAL ANALYSIS")
    print("=" * 35)
    avg = calculate_average(marks_data)
    print(f"Class Average: {avg:.2f}")
    
    median = calculate_median(marks_data)
    print(f"Class Median: {median}")
    
    top_student, max_score = find_max_score(marks_data)
    print(f"Highest Score: {max_score} (by {top_student})")
    
    min_student, min_score = find_min_score(marks_data)
    print(f"Lowest Score: {min_score} (by {min_student})")
    # (End of task 3 deliverable)
    
    # --- Task 4: Grade Assignment & Distribution ---
    student_grades, grade_dist = assign_grades(marks_data)
    print("\n--- Grade Distribution ---")
    for grade, count in grade_dist.items():
        print(f"Grade {grade}: {count} student(s)")
    # (End of task 4 deliverable)
    
    # --- Task 5: Pass/Fail Filter ---
    filter_pass_fail(marks_data)
    
    # --- Task 6: Results Table ---
    print_results_table(marks_data, student_grades)
    # (End of task 6 deliverable)
    
    # --- Bonus Task Prompt ---
    while True:
        save_choice = input("\n[Bonus] Save results to CSV? (y/n): ").lower()
        if save_choice == 'y':
            save_results_to_csv(marks_data, student_grades)
            break
        elif save_choice == 'n':
            break

def main_menu():
    """
    
    Displays the main menu and handles user input.
    This function contains the main program loop. 
    """
    # Print a welcome message
    print("=" * 40)
    print("  Welcome to the GradeBook Analyzer CLI")
    print("=" * 40)
    
    # Allow user to repeat analysis or exit (while loop)
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Enter Marks Manually")
        print("2. Load Marks from CSV File")
        print("3. Exit Program")
        
        choice = input("Please select an option (1-3): ")
        
        marks_data = {}
        
        if choice == '1':
            # Task 2a
            marks_data = get_manual_marks()
        elif choice == '2':
            # Task 2b
            marks_data = get_csv_marks()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            sys.exit() # Use sys.exit() for a clean exit
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        # If data was loaded (dict is not empty), run the analysis
        if marks_data:
            process_analysis(marks_data)
        
        print("\nReturning to main menu...")


# Main script execution
if __name__ == "__main__":
    main_menu()