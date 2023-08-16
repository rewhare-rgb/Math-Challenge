import random
import time

operators_in_challenge = ("-", "+", "*")
total_questions = 10
time_limit = 100  # Time limit in seconds

def generate_question():
    first_num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    operator = random.choice(operators_in_challenge)
    question = f"{first_num} {operator} {second_num}"
    return question

def evaluate_question(question):
    try:
        answer = eval(question)
        return answer
    except:
        return None 

correct_answers = 0

input("Hit Enter To Start The Math Challenge.")
print("----------")

start_time_of_challenge = time.time()    

for question_num in range(1, total_questions + 1):
    question = generate_question()
    print(f"Question {question_num}: {question}")

    challenger_answer = input("Your answer is: ")

    if time.time() - start_time_of_challenge > time_limit:
        print("\nYour time is up.")
        break

    try:
        challenger_answer = float(challenger_answer)
    except ValueError:
        print("Invalid input. Next question.")
        continue

    correct_answer = evaluate_question(question)  # Changed '==' to '='

    if challenger_answer == correct_answer: 
        print("Correct! Well done.\n")
        correct_answers += 1
    else:
        print("Incorrect answer.")

print("----------")
print("The Math Challenge finished. Thanks for taking part!!")
print(f"You scored {correct_answers} out of {total_questions} questions correctly.")
