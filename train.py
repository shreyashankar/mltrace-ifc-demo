from components import *

import argparse
import logging


### PARSING ARGS ###
parser = argparse.ArgumentParser(description="Run training.")
parser.add_argument("--start", type=str, help="Start date", nargs="?")
parser.add_argument("--end", type=str, help="End date", nargs="?")
args = parser.parse_args()

### SETTING UP LOGGING ###
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

##################### PIPELINE CODE #############################

if __name__ == "__main__":
    start_date = args.start if args.start else "01/01/2020"
    end_date = args.end if args.end else "01/31/2020"
    logging.info(
        f"Running the train pipeline from {start_date} to {end_date}..."
    )

    # Clean and featurize data
    df = load_data(start_date, end_date)
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

    # If training, train a model and save it
    train_df, test_df = train_test_split(features_df)
    train_model(train_df, test_df, feature_columns, label_column)
