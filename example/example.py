from youtube_rag import answer_question

youtube_url = input("Enter YouTube URL: ")

while True:

    question = input("\nAsk your question: ")

    answer = answer_question(
        youtube_url,
        question
    )

    print("\nAI Answer:", answer)

    choice = input(
        "\nDo you want to ask another question? (yes/no): "
    ).strip().lower()

    if choice not in ["yes", "y"]:

        print("Thank you for using YouTube RAG Assistant!")

        break