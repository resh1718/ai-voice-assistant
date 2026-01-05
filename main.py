from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# 🔐 OpenAI API Key (Render la Environment Variable use pannalaam)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_reply(user_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant for a small business. Answer politely and shortly."},
                {"role": "user", "content": user_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Sorry, AI service temporarily unavailable."

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_text = request.form["message"]
        reply = get_reply(user_text)
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
