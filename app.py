from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
database = {}
with open('food.json') as fp:
    database = json.load(fp)

@app.route('/')
def home():
    return render_template('home.template.html', page_title="Home")

@app.route('/food-tracker')
def food_tracker():
    return render_template('food-tracker.template.html', page_title="Food Tracker", all_food=database)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)