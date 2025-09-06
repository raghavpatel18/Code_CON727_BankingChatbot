# Banking Assistant Chatbot

A virtual assistant chatbot that provides information about banking services, built with Python, TensorFlow, and Flask.

## Features

- Answers questions about banking services, accounts, loans, credit cards, and more
- Web interface for easy interaction
- Command-line interface for testing
- Trained on over 30 different banking-related topics
- Responsive design that works on desktop and mobile

## Project Structure

- `banking_chatbot_app.py` - Main application file with chatbot logic
- `banking_data.json` - Dataset with intents, patterns, and responses
- `banking_chatbot.ipynb` - Jupyter notebook for model training
- `main.py` - Entry point to run the Flask web application
- `templates/index.html` - HTML template for the web interface
- `static/styles/style.css` - CSS styling for the web interface

## Requirements

- Python 3.6+
- TensorFlow 2.x
- Keras
- NLTK
- Flask

## Setup and Installation

1. Clone the repository
2. Install the required packages:
   ```
   pip install tensorflow keras nltk flask
   ```
3. Run the Jupyter notebook to train the model:
   ```
   jupyter notebook banking_chatbot.ipynb
   ```
4. Start the web application:
   ```
   python main.py
   ```
5. Open your browser and navigate to http://localhost:5000

## Usage

You can interact with the chatbot through:

1. **Web Interface**: Open your browser and go to http://localhost:5000
2. **Command Line**: Run `python banking_chatbot_app.py` for a terminal-based interface

## Sample Questions

- "How do I open a new account?"
- "What are your loan options?"
- "How do I apply for a credit card?"
- "Where is the nearest ATM?"
- "What are your current interest rates?"
- "How do I set up online banking?"
- "What is overdraft protection?"

## Customization

To add more intents or modify responses, edit the `banking_data.json` file and retrain the model using the notebook. 