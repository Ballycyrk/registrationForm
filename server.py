from flask import Flask, request, render_template, redirect, flash, session
import re
from time import gmtime, strftime, strptime
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^.*\d+.*[A-Z]+.*$')
BIRTHDAY_REGEX = re.compile(r'^\d{2}[\-]\d{2}[\-]\d{4}$')
app = Flask(__name__)
app.secret_key='GoodTimesRoll'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/registration', methods=['POST'])
def validate():
  counter = 0
  flash('')
  '''
  flash is tacked onto the end of the session so I needed to insert a blank
  session.  Without it you can't safely iterate through session.  If no flash
  existed when starting to iterate and then a flash is added, the iteration
  errors out because the size of the session list changes.
  '''
  if request.form['password'] != request.form['con_password']:
    flash("Confirmation does not match Password, please re-enter.")
    counter += 1
  elif len(request.form['password']) < 9:
    flash("Password must be at least 9 characters long")
    counter += 1
  elif not PASSWORD_REGEX.match(request.form['password']):
    flash("Password must contain at least 1 number and one CAPITAL letter.")
  if not NAME_REGEX.match(request.form['first_name']):
    flash('Your first name can only contain letters. (Sorry.)')
    counter += 1
  if not NAME_REGEX.match(request.form['last_name']):
    flash('Your last name can only contain letters. (Sorry.)')
    counter += 1
  if not EMAIL_REGEX.match(request.form['email']):
    flash('Not a valid email.')
    counter += 1
  if not BIRTHDAY_REGEX.match(request.form['birthday']):
    print request.form['birthday']
    flash('Enter Birthdate in MM-DD-YYYY format. (i.e. 06-13-2010)')
    counter += 1
  else:
    date1 = strftime("(%m-%d-%Y)")
    birth = strptime(request.form['birthday'], "%m-%d-%Y")
    if strptime(date1, "(%m-%d-%Y)") > birth:
      session['Birthdate'] = request.form['birthday']
    else:
      flash("No one born in the future can type today, please try again.")
      counter += 1
  session['First_name'] = request.form['first_name']
  session['Last_name'] = request.form['last_name']
  session['Email'] = request.form['email']
  session['Password'] = request.form['password']
  for k in session:
    if len(session[k]) == 0:
      flash("{} can't be left blank.".format(k))
      counter += 1
  if counter != 0:
    return redirect('/')
  else:
    flash('Thank you for submitting your information!')
    return redirect('/')
app.run(debug=True)
