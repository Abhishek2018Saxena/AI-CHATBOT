from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hi! How can I help you?"
    elif "your name" in user_input.lower():
        return "I am an AI chatbot created by Abhishek."
    elif "how are you" in user_input.lower():
        return "I am fine! Thanks for asking."
    elif "what is ai" in user_input.lower():
        return "AI means Artificial Intelligence."
    elif "who created you" in user_input.lower():
        return "I was created by Abhishek as a mini project."
    elif "bye" in user_input.lower():
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form["msg"]
    return chatbot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)