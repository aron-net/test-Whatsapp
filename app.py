
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAOJaleRiHUBO9jeztXhRH9F0lP4lEZCpVODiIfUDXSXfmYL7VYeSxZC4ZA8a4BKLecKH31ECkXShaB5xvY3QYl2XwZB3kyd3e11ToPaoKFKUMBhdipWWoFQzG9zVh3ZAZCQ0ivg1vlzBG4y381wSN9vGTT0n3kPaSgzH7XZA26mVk5TY3ZAZA9lfpwUhq0oIthmDFHzHZCqBSvIZCZBDSlt6RUZD"
RECIPIENT_PHONE_NUMBER = "256773294150"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():

    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_PHONE_NUMBER,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://graph.facebook.com/v19.0/277759672094284/messages",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return "Message sent successfully!"
    else:
        return "Error sending message: " + response.text

if __name__ == '__main__':
    app.run(debug=True)
