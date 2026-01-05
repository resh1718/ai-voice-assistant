import os
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# OpenAI client (API key taken automatically from environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_reply(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for a small business."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, AI service temporarily unavailable."

@app.route("/", methods=["GET", "POST"])
def index():
    reply = None
    if request.method == "POST":
        user_message = request.form.get("message")
        if user_message:
            reply = get_reply(user_message)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
