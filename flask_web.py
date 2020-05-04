from flask import Flask, render_template

app = Flask(__name__, template_folder='/root/web')
app._static_folder = "/root/web/static"

@app.route("/")
def index():
	return "Flask App"

@app.route("/afy")
def afy():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

