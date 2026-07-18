import os
from flask import Flask

app = Flask(__name__)

# Vulnerability 1: Hardcoded Mock API key (should use environment variables), high entropy key so gitleak can detect
# SUPER_SECRET_API_KEY = ""
# it's now removed so that gitleak will not detect it even in comments.

API_KEY = os.environ.get("API_KEY")  # Use environment variable for API key


@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)