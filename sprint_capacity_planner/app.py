import json
import os
import pathlib

import flask
import flask_cors

IS_DEVELOPMENT = os.getenv("FLASK_ENV", "") == "development"

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="../web_client/dist")

if IS_DEVELOPMENT:
    flask_cors.CORS(app)


def load_capacity_plans():
    return json.loads(pathlib.Path("./capacity_plans.json").read_text())


@app.route("/")
def get_web_client():
    if IS_DEVELOPMENT:
        response = flask.redirect("http://localhost:8080/")
    else:
        response = flask.send_from_directory("../web_client/dist", "index.html")

    return response


@app.route("/sprints")
def get_all_capacity_plans():
    return load_capacity_plans()


@app.route("/sprints/<uuid:sprint_id>")
def get_capacity_plan_for_sprint(sprint_id):
    sprint_id = str(sprint_id)
    capacity_plans = load_capacity_plans()

    if sprint_id not in capacity_plans:
        return 404
    else:
        return capacity_plans[sprint_id]


if __name__ == "__main__":
    app.run()
