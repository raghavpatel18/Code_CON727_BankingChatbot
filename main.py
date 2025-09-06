import os
import sys
from flask import Flask
from flask import render_template, request

# Import the chatbot application
from banking_chatbot_app import app as chatbot_app

if __name__ == '__main__':
    # Run the Flask app
    chatbot_app.run(debug=True, host='0.0.0.0', port=5000)
