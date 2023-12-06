import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hey there..."

    if p_message == "roll":
        return str(random.randint(1, 6))

    if p_message == "!help":
        return "I'm here to solve your problems"

    return "i didn't understand what you say!"


professional_responses = [
    "Thank you for your input. I'm currently generating your response. Please take a moment as I prepare the information for you.",
    "I appreciate your message. I'm working on providing you with a thoughtful response. Kindly hold on for a moment.",
    "Your request is important to me. I'm in the process of generating a response tailored to your needs. Thank you for your patience.",
    "Acknowledged! I'm working on formulating a comprehensive response for you. Your patience is greatly appreciated.",
    "Thank you for reaching out. I'm here to assist you, and I'm currently compiling the information you need. Please bear with me for a moment.",
    "I've received your message, and I'm actively working on crafting a detailed response. Your understanding is valued during this process.",
    "Your inquiry is important to me. I'm currently in the process of generating a response that addresses your needs. Thank you for your understanding.",
    "Thanks for your message. I'm committed to providing you with a well-thought-out response. Please remain patient as I work on this for you.",
    "I appreciate your communication. I'm currently formulating a response to address your query. Your patience is sincerely valued.",
    "Your input is noted, and I'm diligently working on generating a response tailored to your requirements. Thank you for your patience and understanding.",
    "I'm on it! Your message is receiving my full attention, and I'm actively working to provide you with a comprehensive response. Thank you for your patience.",
    "Noted! I'm working diligently to gather the information needed for your inquiry. Your understanding and patience are highly appreciated.",
    "Thank you for getting in touch. I'm currently crafting a response that addresses your concerns. Please allow me a moment to provide you with the information you need.",
    "Your message is important, and I'm focused on delivering a detailed response. I appreciate your patience as I work through this process.",
    "I'm actively processing your request and formulating a response tailored to your needs. Thank you for your patience and understanding during this time.",
    "I appreciate your patience as I work on providing you with a thorough and accurate response. Your understanding is crucial, and I'm committed to addressing your needs.",
    "Thank you for your message. I'm in the process of gathering the necessary details to provide you with a well-informed response. Your patience is valued.",
    "Your inquiry is a priority, and I'm actively working on delivering a response that meets your expectations. Thank you for your understanding and patience.",
    "I'm actively working on your request and will ensure to provide you with a comprehensive response. Your patience is sincerely appreciated.",
    "Thank you for your message. I'm currently in the process of formulating a response that addresses your specific needs. Your understanding during this time is important to me.",
]
