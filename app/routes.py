from app import app, mail
from flask_mail import Message
from flask import render_template, flash
from app.order import OrderForm


@app.route('/', methods=['GET', 'POST'])
def main_site():
    order = OrderForm()
    if order.validate_on_submit():

        return render_template('index.html', form=order)
    return render_template('index.html', form=order)

def send_email(sender, text):
    msg = Message("Заказ", sender=sender, recipients="mrfranklin42@gmail.com")
    msg.body = text_body
