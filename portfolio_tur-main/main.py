# Import
from flask import Flask, render_template, request, redirect, url_for
from models import db, Feedback

app = Flask(__name__)

# Veritabanı yapılandırması
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    react = request.form.get('react')
    return render_template('index.html', 
                           button_python=button_python, 
                           button_discord=button_discord,
                           button_html=button_html,
                           react=react,
                           button_db=button_db)

# Feedback sayfası
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        feedback_entry = Feedback(email=email, text=text)
        db.session.add(feedback_entry)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('feedback.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for your feedback!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
