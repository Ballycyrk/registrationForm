from flask import Flask, request, render_template, redirect, flash, session
import re
EMAIL_REGEX =
app = Flask(__name__)
app.secret_key='GoodTimesRoll'
@app.route('/')
def index():
  return render_template('index.html')
app.run(debug=True)
