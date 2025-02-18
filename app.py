from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Corrected Quiz Data Structure
quizzes = {
    "python_basics": {
        "title": "Python Basics Quiz",
        "questions": [
            {"question": "What is the output of print(2 * 3)?", "options": ["5", "6", "7"], "answer": "6"},
            {"question": "Which keyword is used to define a function in Python?", "options": ["func", "def", "define"], "answer": "def"},
            {"question": "What data type is the result of: 3 / 2 in Python 3?", "options": ["int", "float", "str"], "answer": "float"},
            {"question": "Which of the following is a mutable data type in Python?", "options": ["tuple", "list", "string"], "answer": "list"},
            {"question": "What does the `len()` function return?", "options": ["The last element", "The number of elements", "The first element"], "answer": "The number of elements"},
            {"question": "Which of these is used to handle exceptions in Python?", "options": ["try-except", "catch-error", "handle"], "answer": "try-except"},
            {"question": "What will `print(type(10))` return in Python?", "options": ["float", "int", "str"], "answer": "int"},
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', quizzes=quizzes)

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    # ✅ Ensure quiz exists
    quiz = quizzes.get(quiz_id)
    if quiz is None:
        return "Quiz not found", 404

    questions = quiz.get("questions", [])

    if request.method == 'POST':
        score = sum(1 for i, q in enumerate(questions) if request.form.get(f'question_{i}') == q['answer'])
        return render_template('result.html', score=score, total=len(questions))

    return render_template('quiz.html', quiz=quiz, quiz_id=quiz_id, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
