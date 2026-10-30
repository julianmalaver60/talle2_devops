from flask import Flask, abort, jsonify

import funtions as f

application = Flask(__name__)
data = f.load_file("./heroes.csv")


@application.route("/")
def index():
    return jsonify(data)


@application.route("/<string:id_heroe>")
def heroe(id_heroe):
    if id_heroe not in data:
        abort(404, description="Heroe no encontrado")
    return jsonify(data[id_heroe])


if __name__ == "__main__":
    application.run(port=5000, debug=True)
