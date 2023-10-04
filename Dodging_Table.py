import random
import time

print('Welcome to my Dodging Math Quiz')
def generate_puzzle():
    """Generate a math puzzle."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/', '**', '%', '//'])
    
    # Create the puzzle and calculate the solution
    puzzle = f"{num1} {operator} {num2}"
    solution = eval(puzzle)
    
    return puzzle, solution

def operator_info():
    ad = '+  Addition\n'
    sub ='-  Subtraction\n'
    ml = '*  Multiplication\n'
    di = '/  Division\n'
    ex = '** Exponention\n'
    fd = '// Floor Division (Remove Decimal)\n'
    mo = '%  Division  (Ans is round off to the nearest whole number)'
    print('The Sign of Basic Mathamatical Operation: ')
    print(ad, sub, ml, di, ex, fd, mo)



print(10 / 3)


def main():
    print("Welcome to the Math Puzzle Generator!")
    user = int(input("Please specify the number of questions you'd like to tackle: "))
    score = 0  # Initialize score
    
    for _ in range(user):
        # Generate a new puzzle
        puzzle, solution = generate_puzzle()

        # Start the timer
        start_time = time.time()

        # Prompt user for the answer
        user_answer = input(f"\nSolve the puzzle: {puzzle} = ")

        # Stop the timer
        end_time = time.time()
        time_taken = end_time - start_time

        # Check if the answer is a valid integer
        try:
            user_answer = float(user_answer)
            # Check if the answer is correct
            if user_answer == solution:
                print(f"Correct! Time taken: {time_taken:.2f} seconds")
                score += 1
            else:
                print(f"Wrong! The correct answer is {solution}. Time taken: {time_taken:.2f} seconds")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print(f"\nYour final score is: {score} out of {user}.")
if __name__ == "__main__":
    main()