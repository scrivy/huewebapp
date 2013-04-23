from flask import Flask
from flask import render_template
from hue import Hue

h = Hue();
h.station_ip = "192.168.1.100"
h.get_state();
l = h.lights.get('l1')

#l.on()
#l.bri(255)

app = Flask(__name__)

@app.route("/")
def hello(name=None):
	return render_template('jshtml.html')

@app.route('/changecolor/<int:red>/<int:green>/<int:blue>')
def changecolor(red,green,blue):
	l.rgb(red, green, blue)
	return 'pray'

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=False,port=80)
