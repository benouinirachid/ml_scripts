import argparse
import pickle


parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--features",
    type=str,
    dest="features",
    required=True,
    help="list of feeatures delimited by ',' .",
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
features = args.features
model_path = args.model_path


if __name__ == "__main__":
    # Make prediction by using the trained model
    features_vector = [float(item) for item in features.split(",")]
    model = pickle.load(open(model_path, "rb"))
    predicted_y = model.predict([features_vector])
    print("#INFO: the predicted value  is :", predicted_y[0])
