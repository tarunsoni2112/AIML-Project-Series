import random

# This dictionary will store our chatbot's responses
responses = {
    "admission procedure": "To apply for admission, you need to visit our website and fill out the application form. Once completed, you need to submit your application along with the required documents.",
    "admission requirements": "For admission, you need to have a valid passport, an IELTS score of at least 6.0, a high school diploma or equivalent, and proof of financial support.",
    "admission deadline": "The deadline for submitting applications for admission is April 15th. However, early applications are encouraged.",
    "fees structure": "The fees structure for international students is detailed on our website. It includes tuition fees, accommodation fees, and miscellaneous fees.",
    "accommodation options": "We offer a range of accommodation options on and off campus, including single, double, and triple rooms. These options cater to various needs and preferences.",
    "facilities available": "Our campus offers state-of-the-art facilities such as modern classrooms, a library, sports facilities, and recreational areas. Additionally, we have an excellent wi-fi network.",
    "healthcare services": "International students are entitled to free healthcare services on campus. These services include consultations with a doctor, lab tests, and prescription medication.",
    "security measures": "We prioritize student safety and security. Our campus has security personnel on patrol and we encourage students to report any suspicious activities or unfamiliar faces.",
    "emergency contacts": "In case of an emergency, you can contact the International Students' Office, the security personnel on campus, or the emergency contact number provided to you.",
    "college life": "Life at our college is a rich mix of academic, cultural, and social experiences. We organize regular events, clubs, and sports activities for students to participate in.",
    "international students community": "We have a vibrant international student community. Students from diverse backgrounds share their experiences, knowledge, and traditions. This enriches our learning environment and fosters friendships across borders.",
    "past students": "We have a strong network of past students who have excelled in their academic and professional careers. They are always available to offer guidance and support to current students."
}

def get_response(question):
    """Returns the appropriate response to the given question"""
    lower_question = question.lower()
    for keyword, response in responses.items():
        if keyword in lower_question:
            return response
    return random.choice([
        "Sorry, I could not find an answer to your question. Could you please rephrase your question?",
        "I'm not sure how to respond to that. Can you ask a different question?",
        "Hmm, that's an interesting question. Unfortunately, I don't have an answer for that."
    ])

print("Welcome to the college admission Q&A chatbot!")
while True:
    user_question = input("Please ask your question: ")
    if user_question.lower() == "exit":
        break
    response = get_response(user_question)
    print(response)