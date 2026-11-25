from flask import Flask, render_template, redirect
from gpiozero import LED
import random

app = Flask(__name__)

led = LED(19)

lista_curiosidades = [
    "Eu gosto de pão.",
    "Sou bom a programar.",
    "Tenho um irmão e quatro primos.",
    "Tenho duas gatas."
    ]

visitas = 0

@app.route('/')
def index():
    global visitas
    curiosidade = random.choice(lista_curiosidades)
    visitas += 1
    if led.is_lit:
        led_status = "On"
    else:
        led_status = "Off"
    return render_template("index.html", led_status=led_status, visitas=visitas, curiosidade=curiosidade)

@app.route('/led/<string:status>')
def led_page(status):

    if status == "on":
        led.on()
        return redirect('/')
    elif status == "off":
        led.off()
        return redirect('/')
    else:
        return "Error"

app.run(host="0.0.0.0", port=8081, debug="True", use_reloader=False)
