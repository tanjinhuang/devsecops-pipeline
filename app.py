import os
from flask import Flask

app = Flask(__name__)

# Vulnerability 1: Hardcoded API key (should use environment variables)
SUPER_SECRET_API_KEY = "sk-proj-abc123def456ghi789jkl012mno345pqr678stu901vwx234"


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)