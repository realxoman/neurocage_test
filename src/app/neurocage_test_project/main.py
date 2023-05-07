from random import random, choice, randint
from time import sleep

from flask import Flask, jsonify

app = Flask(__name__)


FAIL_RATE = 0.25
SENSOR_DATA = [1, 2, 3]  # Bad, Ok, Perfect


@app.route("/data/<int:id>/")
def cage_health(id):
    is_working = random() >= FAIL_RATE

    sleep(randint(1000, 3000) / 1000)

    if not is_working:
        return jsonify({"cage_id": id, "status": "N/A"}), 503

    return jsonify({"cage_id": id, "status": choice(SENSOR_DATA)}), 200


if __name__ == "__main__":
    app.run(port="8000")