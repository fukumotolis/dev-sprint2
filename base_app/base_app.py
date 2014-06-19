from flask import Flask, flash
import flask.views
import os 

app = flask.Flask(__name__) # i don't understand name

app.secret_key = "lettuce"


class Main(flask.views.MethodView):
	def get(self):
		pass

	def post(self):
		pass


class Remote(flask.views.MethodView):	# what's a class?
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return self.get()

add.app_url_rule('/',
	view_func=Main.as_view('index'),
	methods=['GET', 'POST'])

app.add_url_rule('/remote/', 
	view_func=Remote.as_view('main'), 
	methods=['GET', 'POST'])	
# i have no idea what's happening
app.debug = True
app.run()	# is this invoking the class?