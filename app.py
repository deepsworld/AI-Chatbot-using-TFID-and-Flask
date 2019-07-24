from flask import Flask, render_template, jsonify, request
import os
import traceback
from tfidf_bot import bot_engine
from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms.validators import InputRequired, URL



#initalize our flask app
app = Flask(__name__)
app.config['SECRET_KEY']= '123'

class LoginForm(Form):
    query = StringField('Enter query : ', validators=[InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():	
	form = LoginForm()
	query = ''
	if form.validate_on_submit():
		query = form.query.data
		return render_template("success.html", url=form.query.data, response=bot_engine(query))
	return render_template('index.html', form=form)

@app.route('/request', methods=['GET', 'POST'])
def response():	
	try:
		query = request.json[0]['query']
		#print(query)
		return jsonify('response:' + bot_engine(query))
	except:
		return jsonify({'trace': traceback.format_exc()})

	
	
@app.route('/home')
def hello():
    return "Why here bro?"

if __name__ == "__main__":

    #decide what port to run the app in
    port = int(os.environ.get('PORT', 5000))
    #run the app locally on the givn port
    app.run(host='0.0.0.0', port=port, debug = True)








	




   

