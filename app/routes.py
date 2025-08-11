from flask import request, url_for, render_template, redirect
from app import app
from datetime import datetime


@app.route('/')
def home():
    months = {
        "January": "января", "February": "февраля", "March": "марта", "April": "апреля",
        "May": "мая", "June": "июня", "July": "июля", "August": "августа",
        "September": "сентября", "October": "октября", "November": "ноября", "December": "декабря"
    }
    days = {
        "Monday": "Понедельник", "Tuesday": "Вторник", "Wednesday": "Среда",
        "Thursday": "Четверг", "Friday": "Пятница", "Saturday": "Суббота", "Sunday": "Воскресенье"
    }
    time = datetime.now()
    return render_template('index.html', current_time=time,months=months,days=days)


@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'},
        {'name': 'David', 'role': 'Tester'},
        {'name': 'Eva', 'role': 'Business Analyst'},
        {'name': 'Frank', 'role': 'DevOps Engineer'},
        {'name': 'Grace', 'role': 'UI/UX Designer'},
        {'name': 'Hannah', 'role': 'Data Scientist'},
        {'name': 'Ian', 'role': 'System Administrator'},
        {'name': 'Jack', 'role': 'Product Owner'}
    ]

    return render_template('about.html',team_members=team_members)


@app.route('/contact')
def contact():
    customer_care_department = [
        {
            'name': 'Employee 1',
            'position': 'Customer Service Representative',
            'contact_info': {
                'email': 'employee1@example.com',
                'phone': '123-456-7890'
            }
        },
        {
            'name': 'Manager Anton',
            'position': 'Customer Support Specialist',
            'contact_info': {
                'email': 'employee2@example.com',
                'phone': '123-456-7891'
            }
        },
        {
            'name': 'Employee 3',
            'position': 'Technical Support',
            'contact_info': {
                'email': 'employee3@example.com',
                'phone': '123-456-7892'
            }
        },
        {
            'name': 'Employee 4',
            'position': 'Customer Success Manager',
            'contact_info': {
                'email': 'employee4@example.com',
                'phone': '123-456-7893'
            }
        },
        {
            'name': 'Employee 5',
            'position': 'Help Desk Technician',
            'contact_info': {
                'email': 'employee5@example.com',
                'phone': '123-456-7894'
            }
        },
        {
            'name': 'Employee 6',
            'position': 'Customer Experience Specialist',
            'contact_info': {
                'email': 'employee6@example.com',
                'phone': '123-456-7895'
            }
        },
        {
            'name': 'Employee 7',
            'position': 'Client Relations Manager',
            'contact_info': {
                'email': 'employee7@example.com',
                'phone': '123-456-7896'
            }
        },
        {
            'name': 'Employee 8',
            'position': 'Support Team Lead',
            'contact_info': {
                'email': 'employee8@example.com',
                'phone': '123-456-7897'
            }
        },
        {
            'name': 'Employee 9',
            'position': 'Customer Feedback Analyst',
            'contact_info': {
                'email': 'employee9@example.com',
                'phone': '123-456-7898'
            }
        },
        {
            'name': 'Employee 10',
            'position': 'Service Quality Coordinator',
            'contact_info': {
                'email': 'employee10@example.com',
                'phone': '123-456-7899'
            }
        }
    ]
    return render_template('contact.html',customer_care_department=customer_care_department)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        # name = request.form.get('name')
        # email = request.form.get('email')
        succsess_message = 'Your message has been sent successfully!'
        return render_template('contact.html', message=succsess_message)
    else:
        return redirect(url_for('contact'))
