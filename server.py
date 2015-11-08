from flask import Flask, request, render_template, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
app.secret_key='GoodTimesRoll'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/registration', methods=['POST'])
def validate():
  print '******************************************************'
  counter = 0
  flash('')
  if request.form['password'] != request.form['con_password']:
    flash("Confirmation does not match Password, please re-enter.")
    counter += 1
  session['First_name'] = request.form['first_name']
  session['Last_name'] = request.form['last_name']
  session['Email'] = request.form['email']
  session['Password'] = request.form['password']
  for k in session:
    if len(session[k]) == 0:
      print k
      flash("{} can't be left blank.".format(k))
      counter += 1
  if counter != 0:
    return redirect('/')
  else:
    return render_template('success.html')
app.run(debug=True)
