from teacher import AITeacher

teacher = AITeacher("physics_dataset.json")

print("=" * 50)
print("Physics AI Teacher")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    question = input("\nAsk Physics Question: ")

    if question.lower() == "exit":
        break

    answer = teacher.answer_question(question)

    print("\nAI Teacher:")
    print(answer)
