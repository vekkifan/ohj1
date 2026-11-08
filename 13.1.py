from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:numero>', methods=['GET'])
def tarkista_alkuluku(numero):
    tulos = onko_alkuluku(numero)
    vastaus = {
        "Number": numero,
        "isPrime": tulos
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
