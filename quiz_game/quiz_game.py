def quiz_game(questions):
    wrong_answers = []
    score = 0
    total = len(questions)
    valid_options = ["A", "B", "C", "D"]
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}/{total}:")
        print(q["question"])
        print("\n".join(q["options"]))
        while True:     # keep asking until valid
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in valid_options:
                break                                        
            else:
                print("⚠️ Invalid input! Please enter A, B, C or D only.")
        if answer == q["answer"]:
            score +=1
        else:
            wrong_answers.append((q["question"],answer,q["answer"]))
    print(f"Your score is {score } out of {len(questions)}.")
    print(f"Your percentage is {score/len(questions)*100:.2f}%")

    if wrong_answers:
        print("The questions that you got wrong are :")
        for i,j,k in wrong_answers:
            print(f"{i} \n Your answer : {j} ❌ \n Should have been : {k} ✅\n")

    if score == len(questions):
        print("Congratulations! You got all the questions correct! 🎉")
    else:
        print("Better luck next time! Keep practicing! 💪")


questions = [
    {
        "question": "What is the capital of India?",
        "options"  : ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer"   : "B"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options"  : ["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
        "answer"   : "C"
    },
    {
        "question": "What does CPU stand for?",
        "options"  : ["A. Central Process Unit", "B. Computer Personal Unit",
                      "C. Central Processing Unit", "D. Core Processing Unit"],
        "answer"   : "C"
    },
    {
        "question": "Which language is used for AI/ML?",
        "options"  : ["A. Java", "B. C++", "C. Python", "D. PHP"],
        "answer"   : "C"
    },
    {
        "question": "What is 2 ** 10?",
        "options"  : ["A. 512", "B. 1024", "C. 2048", "D. 256"],
        "answer"   : "B"
    },
    {
    "question": "Who directed the movie 'Inception'?",
    "options"  : ["A. Steven Spielberg", "B. Christopher Nolan", "C. James Cameron", "D. Quentin Tarantino"],
    "answer"   : "B"
    },
    {
    "question": "Which country won the Cricket World Cup in 2011?",
    "options"  : ["A. Australia", "B. England", "C. India", "D. Sri Lanka"],
    "answer"   : "C"
    },
    {
    "question": "What is the speed of light in vacuum?",
    "options"  : ["A. 3 x 10^8 m/s", "B. 3 x 10^6 m/s", "C. 3 x 10^5 km/s", "D. 1.5 x 10^8 m/s"],
    "answer"   : "A"
    },
    {
    "question": "Which Python data type is immutable?",
    "options"  : ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
    "answer"   : "D"
    },
    {
    "question": "Which element has the chemical symbol 'Na'?",
    "options"  : ["A. Nitrogen", "B. Sodium", "C. Neon", "D. Nickel"],
    "answer"   : "B"
    }

]
print("\n ------- Welcome to the Quiz Game ------- \n")
quiz_game(questions)