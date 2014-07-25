from flask import render_template, request
from app import app
import sys
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname' : 'Jatin'} #Fake user
	sys.path.append("D:\Users\jkathuri\projects\microblog\microblog_flask_master_kit\Lib\site-packages")
	path = sys.path
	
	module= sys.modules
	posts = [
			{
				'author' : {'name' : 'Alan Turing'},
				'content' : 'One of the best computer scientist world has ever produced.'
			},
			{
				'author' : {'name' : 'Gauss'},
				'content' : 'Invented Game thoery at the age of 15'
			}]
	return render_template("index.html", user=user, title='Welcome', posts=posts)
	

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login Requesested for ' + form.openid.data + ' and Remember me = ' + str(form.remember_me.data))
		return redirect('/index')
	user = { 'nickname' : 'Jatin'} 
	return render_template('login.html',title='signin',form=form,user=user)
	
