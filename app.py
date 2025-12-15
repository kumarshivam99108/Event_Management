from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Ensure the instance folder exists
if not os.path.exists('instance'):
    os.makedirs('instance')

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Registration {self.name}>'

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            event_type = request.form['event']
            message = request.form['message']

            # Create new registration
            new_registration = Registration(
                name=name,
                email=email,
                phone=phone,
                event_type=event_type,
                message=message
            )

            # Add to database
            db.session.add(new_registration)
            db.session.commit()
            return redirect(url_for('after'))

        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while processing your registration"

    return render_template('register.html')

@app.route('/after')
def after():
    return render_template('after.html')

@app.route('/check_db')
def check_db():
    try:
        # Test database connection
        db.session.execute(db.text('SELECT 1'))
        
        # Get all registrations
        registrations = Registration.query.all()
        
        # Format registrations as HTML
        html = '<h2>Database Connection: Success</h2>'
        html += '<h3>Current Registrations:</h3>'
        
        if registrations:
            html += '<ul style="list-style: none; padding: 20px;">'
            for reg in registrations:
                html += f'''
                    <li style="margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
                        <strong>Name:</strong> {reg.name}<br>
                        <strong>Email:</strong> {reg.email}<br>
                        <strong>Phone:</strong> {reg.phone}<br>
                        <strong>Event:</strong> {reg.event_type}<br>
                        <strong>Date:</strong> {reg.date_registered}<br>
                        <strong>Message:</strong> {reg.message or 'No message provided'}<br>
                    </li>'''
            html += '</ul>'
        else:
            html += '<p>No registrations found.</p>'
            
        return html
        
    except Exception as e:
        return f'<h2>Database Error:</h2><p>{str(e)}</p>'

if __name__ == '__main__':
    app.run(debug=True)
