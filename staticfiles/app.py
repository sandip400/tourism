from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Function to extract data from a given webpage
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text from the webpage
        page_text = ' '.join(p.text for p in soup.find_all('p'))  # Get all paragraphs
        return page_text[:500] + "..."  # Limit response size
    except Exception as e:
        return f"Error: {str(e)}"

# Chatbot Route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    if "hello" in user_message:
        bot_response = "Hi there! How can I assist you today?"
    elif "scrape" in user_message:
        url = "http://127.0.0.1:5500/dip.html"  # Replace with actual URL
        bot_response = scrape_website(url)
    else:
        bot_response = "I'm not sure how to respond to that. Try asking about scraping."

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
