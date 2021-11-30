from components import *
from flask import Flask, request, jsonify

import logging
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    if not data:
        return jsonify({"error": "No data received"}), 400
    if "start" not in data or "end" not in data:
        return jsonify({"error": "Missing start or end"}), 400

    start_date = data["start"]
    end_date = data["end"]

    # Run inference on points in that range
    logging.info(
        f"Running the train pipeline from {start_date} to {end_date}..."
    )

    # Clean and featurize data
    try:
        df = load_data(start_date, end_date)
    except Exception as e:
        return jsonify({"error": "Data loading did not work."}), 400

    clean_df = clean_data(df, start_date, end_date)
    features_df = featurize_data(clean_df)

    feature_columns = [
        "pickup_weekday",
        "pickup_hour",
        "pickup_minute",
        "work_hours",
        "passenger_count",
        "trip_distance",
        "RatecodeID",
        "congestion_surcharge",
        "loc_code_diffs",
    ]
    label_column = "high_tip_indicator"
    _, scores = inference(features_df, feature_columns, label_column)

    res = {
        "start": start_date,
        "end": end_date,
        "scores": scores,
    }

    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
