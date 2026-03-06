from flask import Flask, render_template, request

app = Flask(__name__)

# First page
@app.route('/')
def home():
    return render_template("home.html")

# Calculator page
@app.route('/calculator')
def calculator():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():

    electricity = float(request.form.get('electricity',0))
    petrol = float(request.form.get('petrol',0))
    lpg = float(request.form.get('lpg',0))
    bus = float(request.form.get('bus',0))
    train = float(request.form.get('train',0))

    electricity_emission = electricity * 0.85
    petrol_emission = petrol * 2.31
    lpg_emission = lpg * 3
    bus_emission = bus * 0.1
    train_emission = train * 0.05

    total = electricity_emission + petrol_emission + lpg_emission + bus_emission + train_emission

    if total < 100:
        advice = "Good 👍 Your carbon footprint is low."
    elif total < 300:
        advice = "Try reducing electricity and fuel usage."
    else:
        advice = "High carbon footprint ⚠ Use public transport."

    return render_template(
        "result.html",
        electricity=electricity_emission,
        petrol=petrol_emission,
        lpg=lpg_emission,
        bus=bus_emission,
        train=train_emission,
        total=total,
        advice=advice
    )

if __name__ == "__main__":
    app.run(debug=True)