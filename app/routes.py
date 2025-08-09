from flask import request,url_for,render_template,redirect
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        # name = request.form.get('name')
        # email = request.form.get('email')
        succsess_message = 'Your message has been sent successfully!'
        return render_template('contact.html',message=succsess_message)
    else:
        return redirect(url_for('contact'))