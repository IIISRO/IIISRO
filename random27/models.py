from extensions import db
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    your_name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(20), nullable = False, unique = True)
    services = db.Column(db.String(4), nullable = False)
    budget = db.Column(db.Integer, nullable = False)
    message = db.Column(db.Text)

    def __init__(self, your_name, email, services, budget, message):
        self.your_name = your_name
        self.email = email
        self.services = services
        self.budget = budget
        self.message = message
        
    def save(self):
        db.session.add(self)
        db.session.commit()