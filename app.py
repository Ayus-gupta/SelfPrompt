

from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/generate', methods=['POST'])
def generate():
    # Collect & sanitize inputs
    q1 = request.form.get('q1', '').strip()
    q2 = request.form.get('q2', '').strip()
    q3 = request.form.get('q3', '').strip()
    q4 = request.form.get('q4', '').strip()
    q5 = request.form.get('q5', '').strip()

    # ---------- Validation ----------
    if not all([q1, q2, q3, q4, q5]):
        flash("All questions must be answered before generating the prompt.", "error")
        return redirect(url_for('index'))

    if len(q1) < 5:
        flash("Q1 should clearly describe the task (at least 5 characters).", "error")
        return redirect(url_for('index'))

    if len(q2) < 10:
        flash("Q2 needs enough context for better AI output.", "error")
        return redirect(url_for('index'))

    if len(q3) < 5 or len(q4) < 5 or len(q5) < 5:
        flash("Please provide meaningful answers for all questions.", "error")
        return redirect(url_for('index'))

    # ---------- Success ----------
    return render_template(
        "final_promt.html",
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,
        q5=q5
    )
@app.route('/explain')
def explain():
    return render_template('explain.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
