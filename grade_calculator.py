
import random

def main():
    grades_list = []

    print(" I present the grades list program.\n ")
    print("--- Function to get grades from the user.---")
    while True:
        
        user_input = input(" Pleas enter a grade or one of the grades (or -1 to stop): ")
        
        if user_input == "-1":
            break
        else:
            try:
                grade = float(user_input) 
                grades_list.append(grade)
            except ValueError:
                print("\n Thats not a number between 0-100, Please enter a valid number.")

    print(" This is the list of grades:\n\n", grades_list)



    
    print(" \n--- Function to remove the lowest grade from the list.---")
    print(" i shall be taking away the lowest grade... ")
    if grades_list:  # Check if the list is not empty
        lowest_grade = min(grades_list)
        grades_list.pop(grades_list.index(lowest_grade))
    print(" Here is the list aftertaking away the lowest grade: \n", grades_list)



    print("\n\n--- Function to remove a random grade from the list.---")
     
    print(" Now... I will be taking away a random grade from the list...")
    if grades_list:  
        random_grade = random.choice(grades_list)
        grades_list.remove(random_grade)
    print(" This is the list of grades afterwards: \n", grades_list)


    print("\n--- Function to edit a specific grade.---")
    print(" If you wish to edit a grade, do so now...\n")
    for index, grade in enumerate(grades_list, start=1):
        print(f"{index}: {grade}")

    while True:
        try:
            edit_index = int(input(" Choose from one of those index's to edit (1-based index): ")) - 1
            if 0 <= edit_index < len(grades_list):
                new_grade = float(input(" Enter the new grade: "))
                grades_list[edit_index] = new_grade
                break
            else:
                print(" thats not one of the index's from the list ")
        except ValueError:
            print("Please enter one of the index's.")



    print(" Here is the list of grades after editing:\n", grades_list)




    print("\n---Function to display sorted and reversed grades.---")
    print(" This is sorting and reversing the list...")
    grades_list.sort()
    grades_list.reverse()
    print(" List of grades after sorting and reversing:\n", grades_list)



    print("\n---Function to calculate and print total and average of grades.---")
    print(" Getting the total and average of grades...\n")
    total = sum(grades_list)
    average = total / len(grades_list) if grades_list else 0
    print(" Here is the total of grades:", total)
    print(" this is the average of grades:", average)


    print(" ---made by pablo romero---")




if __name__ == "__main__":
    main()




