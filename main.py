from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	predictions = [
		{
			'name': 'prediction 1', 
			'option1': 'test',
			'option2': 'ok',
			'result': 'ok',
		},
	]

	return render_template('./index.html', predictions=predictions)

if __name__ == '__main__':
	app.run(debug=True)