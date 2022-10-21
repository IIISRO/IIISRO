from flask import render_template, request
from app import app
from models import *
from forms import *

@app.route("/", methods = ["GET", "POST"])
def index():
    post_data = request.form
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data = post_data)
        if form.validate_on_submit():
            contact = Contact(form.your_name.data, form.email.data, form.services.data, form.budget.data, form.message.data)
            contact.save()
    return render_template("index.html", form = form)