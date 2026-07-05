# William Littlefield
# July 2 2026
# P4HW1
# Using loops to process a list of scores and determine the average and letter grade.

# Display "How many scores do you want to enter?" and store the value in a variable
# Begin the loop to get the scores from the user and make it so negatives and grades over 100 is invalid
# Sort the list of scores and remove the lowest score and calculate the avg
# Assign a letter grade based on the 10 point system then display results 

# Create a list for scored
num_score = int(input("How many scores do you want to enter? "))
scores = []

# start the loop for scores
for info in range(1, num_score + 1):
    score = float(input(f"Enter score {info}: "))
    
    while score < 0 or score > 100:
        print("Invalid score!!!! Please enter a score between 0 and 100.")
        score = float(input(f"Enter score {info}: "))
    
    scores.append(score)

# Process the scores   
lowest = min(scores)
scores.remove(lowest)   
average = sum(scores) / len(scores)

#Determine the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

    # Display the results
print("-------------Results-----------------")
print(f"\nLowest: {lowest}")
print(f"Modified list: {scores}")
print(f"Average: {average}")
print(f"Letter grade: {grade}")
print("-------------------------------------")