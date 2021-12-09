# Marvel characters quiz

# List of characters names
characterNames = ["Drax the Destroyer", "Valkyrie", "Mantis", "Hela"]

# Dictionay containing questions ans their corresponding answers
answerOfQuestions = {
    "This character lost his family to Ronan the Accuser. Who suffered this tragic loss?": "Drax the Destroyer",
    "Which character has the ability to manipulate plants?": "Mantis",
    "This character was influenced by the Norse mythological figure, Brynhildr. Who fits this trait?": "Valkyrie",
    "According to the Asgardian culture, who is the goddess of death?": "Hela"}

# List to store answerrs entered by user
userAnswers = []

# Total poitns of the user
totalPoints = 0

# Points related to each question
questions = {"This character lost his family to Ronan the Accuser. Who suffered this tragic loss?": 2,
             "Which character has the ability to manipulate plants?": 1,
             "This character was influenced by the Norse mythological figure, Brynhildr. Who fits this trait?": 4,
             "According to the Asgardian culture, who is the goddess of death?": 3}

# Main quiz


def quiz():
    global answerOfQuestions
    global questions
    global characterNames
    global totalPoints

    # Tell options to user
    print("Choose from these options for each question - \n", characterNames)

    for question in answerOfQuestions.keys():
        print("\nQuestion > ", question)  # Tell question to user
        answer = input("Answer > ")  # Ask for answer
        # if answer is correct compared by questions/answer dictionary, increase total points of the user
        if answerOfQuestions[question] == answer:
            totalPoints += questions[question]

# Show result to the user and correct answers


def result():
    print("\nResult of quiz is ", totalPoints,
          "points out of 10\n")  # Tell points

    # Showing correct answer
    print('Correct answers - ')
    for key in answerOfQuestions:
        print(key, answerOfQuestions[key], sep='\tAnswer = ')


quiz()
result()
