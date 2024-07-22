from flask import Flask, render_template, request, redirect, url_for
from models.models import db, Contact

web = Flask(__name__)

# Database configuration
web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(web)
with web.app_context():
    db.create_all()

#home page route
@web.route('/')
def home():
    return render_template("MyProfile.html")

@web.route('/contact')
def contact():
    return render_template("form.html")



@web.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    
    new_contact = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        message=message
    )
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    
    # Process the form data
    db.session.add(new_contact)
    db.session.commit()
    return redirect(url_for('home'))

@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/projects')
def project():
    return render_template('projects.html')

if __name__ == '__main__':
    web.run(debug=True)