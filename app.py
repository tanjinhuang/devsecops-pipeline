import os
from flask import Flask

app = Flask(__name__)

# Vulnerability 1: Hardcoded API key (should use environment variables)
SUPER_SECRET_API_KEY = "sk-proj-7mKz9XWq2vB4nR1tY6pL3jH8dQ5sC0eG9fA2xZ1vB3nM"


@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)