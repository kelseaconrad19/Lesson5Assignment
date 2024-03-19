# Task 1: Develop a list of questions and answers.
quiz_questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Hamlet'?", "William Shakespeare"),
    ("What is the chemical symbol for gold?", "Au"),
    ("In which year did the Titanic sink?", "1912"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the smallest prime number?", "2"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What element does 'O' represent on the periodic table?", "Oxygen"),
    ("What is the longest river in the world?", "Nile"),
    ("Who is known as the father of computers?", "Charles Babbage"),
    ("What year did World War I begin?", "1914"),
    ("What is the speed of light in a vacuum?", "299,792,458 meters per second"),
    ("Who was the first person to step on the moon?", "Neil Armstrong"),
    ("What is the hardest natural substance on Earth?", "Diamond"),
]


# Task 2: Write a function that quizzes the user and takes their answers.
def quiz(questions):
    score = 0
    for question, answer in quiz_questions:
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            score += 1
            print(f"Correct! Your score is {score}")
        else:
            print(f"Wrong. The correct answer is {answer}.")
# Task 3: Score the quiz and give the user feedback on their performance.


quiz(quiz_questions)
