from flask import Flask, render_template, request

app = Flask(__name__)

def get_reply(text):
    text = text.lower()
    if "time" in text or "open" in text:
        return "We are open from 9 AM to 8 PM."
    elif "fees" in text:
        return "Fees details will be shared during visit."
    elif "appointment" in text:
        return "Yes, appointment is available."
    else:
        return "Please contact us for more details."

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_text = request.form["message"]
        reply = get_reply(user_text)
    return render_template("index.html", reply=reply)

app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

