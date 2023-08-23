import os

from jinja2 import Template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

EMAIL_ADDRESS = "poc.reco.luxeroom@gmail.com"


def generate_template(template_path, customer, cart_articles, recommended_articles):
    with open(template_path, 'r', encoding='utf-8') as file:
        template = Template(file.read())
    with open("template/style.css", "r") as css_file:
        css_content = css_file.read()
    html_content = template.render(customer=customer, cart_articles=cart_articles,
                                   recommended_articles=recommended_articles)
    html_content = html_content.replace("</head>", f"<style>{css_content}</style></head>")
    return html_content


def send_email(customer, cart_articles, recommended_articles):
    """
    Sends email to customer with details about their shopping cart and recommended items
    :param customer: info about the customer (dict)
    :param cart_articles: info about the articles from the cart (dict)
    :param recommended_articles: info about the recommended articles (dict)
    """
    email_subject = "Don't forget your shopping cart!"
    template_path = "template/email_template.html"
    email_body = generate_template(template_path, customer, cart_articles, recommended_articles)

    message = Mail(
        from_email=EMAIL_ADDRESS,
        to_emails=EMAIL_ADDRESS,
        subject=email_subject,
        html_content=email_body)
    message.encoding = 'utf-8'

    try:
        # The API key has to be set in the SENDGRID_API_KEY environment variable
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Status code: {response.status_code}")
    except Exception as e:
        print(e.message)

