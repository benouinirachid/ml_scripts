import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle


parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--input_data",
    type=str,
    dest="input_data",
    required=True,
    help="input data file.",
)

parser.add_argument(
    "-t",
    "--target",
    type=str,
    dest="target",
    required=True,
    help="target feature from the data file.",
)

parser.add_argument(
    "-m",
    "--model_path",
    type=str,
    dest="model_path",
    required=True,
    help="path for loading the model.",
)

args = parser.parse_args()
input_data = args.input_data
model_path = args.model_path
target = args.target

def eval_model(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    # Evaluation of model on a set of data
    data = pd.read_csv(input_data, sep=",")
    # The predicted column is "quality" which is a scalar [3, 9]
    data_x = data.drop([target], axis=1)
    data_y = data[[target]]
    model = pickle.load(open(model_path, "rb"))
    predicted_y = model.predict(data_x)
    (rmse, mae, r2) = eval_model(data_y, predicted_y)
    print("#INFO:  RMSE: %s" % rmse)
    print("#INFO:  MAE: %s" % mae)
    print("#INFO:  R2: %s" % r2)
    print("#INFO: Model is succefully evaluated!")
