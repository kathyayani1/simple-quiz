questions = ("1.What is the smallest planet in our solar system?",
             "2.What is the capital of India?",
             "3.What is the Jersy number of Virat kohli?")
options = (("A.Mars", "B.Mercury", "C.Earth", "D.Jupiter"),
           ("A.New Delhi", "B.Hyderabad", "C.vijayawada", "D.Bengaluru"),
           ("A.45", "B.18", "C.99", "D.15"))
answers = ("B", "A", "B")
score = 0
question_num = 0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter the Answer:").upper()
    '''guesses.append(guess)'''
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("      RESULTS     ")
print("Your score is " + str(score) + "/" + str(len(questions)))