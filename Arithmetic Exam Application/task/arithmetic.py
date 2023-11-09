import random


# Function to evaluate expressions
def calculate(expression):
    operands = expression.split()
    if len(operands) == 3:
        operand1, operator, operand2 = operands
        operand1 = int(operand1)
        operand2 = int(operand2)
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
    return "Invalid expression"


# Function to generate a random math task
def generate_task():
    # Define the possible operators
    operators = ['+', '-', '*']
    # Randomly choose two numbers and an operator
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(operators)
    # Return the task as a string
    return f"{num1} {operator} {num2}"

def choose_difficulty():
    while True:
        try:
            level = int(input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                return level
            else:
                raise ValueError
        except ValueError:
            print("Incorrect format.")

def generate_task_level_2():
    num = random.randint(11, 29)
    return num
def main():
    level = choose_difficulty()
    score = 0

    for _ in range(5):
        if level == 1:
            task = generate_task()
            print(task)
            correct_answer = calculate(task)
        else:
            task = generate_task_level_2()
            print(task)
            correct_answer = task ** 2

        while True:
            try:
                user_answer = input()
                if not user_answer.isdigit() and not (user_answer.startswith('-') and user_answer[1:].isdigit()):
                    raise ValueError
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Incorrect format.")

        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your mark is {score}/5.")
    if input("Would you like to save the result? Enter yes or no.\n> ").lower() in ['yes', 'y']:
        name = input("What is your name?\n> ")
        with open("results.txt", "a") as file:
            file.write(f"{name}: {score}/5 in level {level} ({'simple operations with numbers 2-9' if level == 1 else 'integral squares of 11-29'})\n")
        print("The results are saved in \"results.txt\".")


# Check if the script is run directly (and not imported)
if __name__ == "__main__":
    main()
