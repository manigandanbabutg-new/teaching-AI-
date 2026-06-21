import json

class AITeacher:

    def __init__(self, dataset_file):
        with open(dataset_file, "r") as file:
            self.knowledge = json.load(file)

    def answer_question(self, question):

        for key in self.knowledge:

            if question.lower() in key.lower():
                return self.knowledge[key]

        return "Sorry, I don't know that answer yet."

    def learn(self, question, answer):

        self.knowledge[question] = answer

        with open("physics_dataset.json", "w") as file:
            json.dump(self.knowledge, file, indent=4)

        return "New knowledge saved successfully."
