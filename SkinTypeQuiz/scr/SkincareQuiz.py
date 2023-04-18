from question_bank import questions
from results import results


class SkincareQuiz:
    def __init__(self):
        self.results = results
        self.questions = questions

    # function to ask question: prints the question text from selected question dictionary,
    # prints the options and labels them from 1-5
    # adds "points" to skin type scoreboard based on options and weights
    def ask_question(self, question_text, options, weights):
        print(question_text)
        for label, option in enumerate(options, 1):
            print(f"{label}. {option}")
        answer = int(input("Select an option: "))
        while answer < 1 or answer > 5:
            print("Please try again.")
            answer = int(input("Select an option: "))
        weights_dict = weights[answer - 1]
        for key in weights_dict:
            self.results[key] += weights_dict[key]

    # function that returns the skin type with the highest number of points from scoreboard
    def get_skin_type(self):
        highest = 0
        your_skin_type = ""
        for type, value in self.results.items():
            if value > highest:
                highest = value
                your_skin_type = type
        return your_skin_type

    # function to run the quiz
    # loops through each question dictionary from the list of dictionaries from question bank
    def run_quiz(self):
        for q in self.questions:
            self.ask_question(q["question"], q["options"], q["weights"], )
        print(f"Your skin type is: {self.get_skin_type().upper()}")
