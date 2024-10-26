# Flask Score Assessment App

This Flask web application allows users to submit their scores in various subjects and calculates their average score, determines pass/fail status, and displays the result. It demonstrates the basics of handling user input, conditional rendering, and URL routing in Flask.

---

## Features

- **Home Page**: Welcomes users to the application.
- **Score Submission**: Allows users to input scores for subjects such as Python, Machine Learning, Statistics, and Data Science.
- **Result Calculation**: Calculates the average score and determines if the user passed or failed based on a 50% threshold.
- **Result Display**: Shows the user's pass/fail status and average score as a percentage.

---

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Framework to create and manage the web application.
- **HTML**: Used for templates (`index.html`, `result.html`, `success.html`).
- **Bootstrap** (Optional): To style the HTML templates for better UI.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/score-assessment-app.git
   cd score-assessment-app

<img width="313" alt="image" src="https://github.com/user-attachments/assets/9fd16877-4805-4123-8fa0-d8536827e1ed">

# Application Workflow
Home Page: Navigate to / to access the home page and start the assessment.
Submit Scores: Enter scores for Python, Machine Learning, Statistics, and Data Science, then submit.
Result Calculation:
The app calculates the average score and determines if it meets the passing threshold of 50%.
Users are redirected to either the success.html or result.html page based on their average score.
Result Display:
/success/<int:score> displays the score, percentage, and pass/fail status.

# Code Overview
app.py
@app.route('/'): Home page.
@app.route('/success/<int:score>'): Displays pass/fail with detailed percentage.
@app.route('/results/<int:score>'): Shows basic pass/fail outcome.
@app.route('/submit', methods=['POST', 'GET']): Handles form submissions to calculate average scores.
HTML Templates
index.html: Input form for scores.
result.html: Displays pass/fail status and score.
success.html: Shows the detailed result with score and percentage.

Usage
Run the app and submit scores for evaluation.
The application will handle routing to display the appropriate result page.
