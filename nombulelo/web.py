from flask import Flask, render_template, request, redirect, url_for
from Contacts import db, Contact

web = Flask(__name__)

# Database configuration
web.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
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
    
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        contact_number = request.form['contact_number']
        message = request.form['message']
        
    if not name or not email or not message:
        return "All fields are required!"
    
#new instance 
    new_contact = Contact(
        name = name,
        surname = surname,
        email = email,
        contact_number = contact_number,
        message = message
    )
    
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