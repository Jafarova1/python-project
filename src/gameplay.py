def play_quiz(questions):
    score = 0
    for q, opts, ans in questions:
        print(q)
        for i, opt in enumerate(opts):
            print(f"{i+1}. {opt}")
        choice = input("Your choice (1-4): ")
        if opts[int(choice)-1] == ans:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {ans}\n")
    print(f"Your total score: {score}/{len(questions)}")
