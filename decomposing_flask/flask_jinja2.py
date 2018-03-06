"""
    This module has one method which relies on
    Jinja to to produce the email content. 
"""
from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime


def render_email(**data):
    """
        The render_email function uses the Template class
        to generate the email using the provided data.

        :param data:
        :return:
    """
    with open('email_template.eml') as f:
        template = Template(f.read())
    return template.render(**data)


data = {  'date': format_datetime(datetime.now())
        , 'to': 'sy_ode@yahoo.com'
        , 'from': 'syeed.ode@gmail.com'
        , 'subject': "You Syeed's Burger"
        , 'name': 'Mr. Ode'
        , 'items': [
                {'name': 'Cheeseburger', 'price': 4.5}
              , {'name': 'Fries', 'price': 2.0}
              , {'name': 'Root Beer', 'price': 3.0}
            ]
        }

print(render_email(**data))
