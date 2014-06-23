from flask import Flask, render_template

# Random comment
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/membership')
def membership():
	return render_template('membership.html')

@app.route('/outreach')
def outreach():
	return render_template('outreach.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/sponsors')
def sponsors():
	return render_template('sponsors.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')
	
if __name__ == '__main__':
	app.debug = True
	app.run()
