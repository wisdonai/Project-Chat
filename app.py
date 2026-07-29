from flask import Flask, render_template, request
from brain import get_response


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    user_message = ""
    chat_response = ""

    if request.method == "POST":
        user_message = request.form.get("message", "")
        chat_response = get_response(user_message)

    return render_template(
        "chat.html",
        user_message=user_message,
        chat_response=chat_response
    )


if __name__ == "__main__":
    app.run(debug=True)