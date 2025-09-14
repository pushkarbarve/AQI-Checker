import os
from flask import Flask, render_template
from dotenv import load_dotenv

# This line loads the environment variables from your .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    # Now you can securely access your API key
    # IMPORTANT: Make sure the variable name in your .env file matches "API_KEY"
    api_key = os.getenv("API_KEY")

    # For this example, I'm just printing it to the console to show it works.
    # In your real code, you would use this key to make an API call.
    print(f"My API Key is: {api_key}")

    # Flask automatically looks for this file in the 'templates' folder
    return render_template('template.html')

# This part is for local testing only
if __name__ == '__main__':
    app.run(debug=True)
