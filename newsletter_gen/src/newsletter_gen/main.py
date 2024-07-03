#!/usr/bin/env python
from newsletter_gen.crew import NewsletterGenCrew

def load_html_template():
    with open('src/newsletter_gen/config/newsletter_template.html', 'r') as file:
        html_template = file.read()

    return html_template

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input('Enter the Topic for your Newsletter: '),
        'personal_message': input('Enter the Personal Message for your Newsletter: '),
        'html_template': load_html_template(),
    }
    NewsletterGenCrew().crew().kickoff(inputs=inputs)