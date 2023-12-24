class ChatBot:
    def __init__(self):
        self.user_name = None
        self.greeted = False
        self.farewelled = False

    def greet(self):
        self.greeted = True
        return "Hello! How can I help you today?"

    def farewell(self):
        self.farewelled = True
        return "Thank you for using the Simple Chatbot. Goodbye!"

    def respond_to_question(self, question):
        if "how are you" in question.lower():
            return "I'm doing great, thank you! How can I help you?"
        elif "what is your name" in question.lower():
            return "My name is Simple Chatbot."
        elif "where are you from" in question.lower():
            return "I'm from the cloud."
        elif "how old are you" in question.lower():
            return "I'm not sure about my age, but I'm still learning!"
        elif "who created you" in question.lower():
            return "I was created by a wonderful developer."
        else:
            return "I'm not sure how to answer that. Can you ask me something else?"

    def process_user_input(self, user_input):
        if not self.greeted:
            return self.greet()
        elif self.farewelled:
            return self.greet()
        else:
            return self.respond_to_question(user_input)


chatbot = ChatBot()

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print(chatbot.farewell())
    else:
        print(chatbot.process_user_input(user_input))