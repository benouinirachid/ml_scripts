# ml_scripts
Ready to use Machine Learning Python Scripts.

# Setup

First you need to install the required python packages.

    pip install -r requirements.txt

# Scripts
Data Loading 

    $ python load_data.py -h
    usage: load_data.py [-h] -u URL -p PATH

    optional arguments:
    -h, --help            show this help message and exit
    -u URL, --url URL     url of data file.
    -p PATH, --path PATH  path to save the file.

Data Processessing 

    $ python process_data.py -h
    usage: process_data.py [-h] -i INPUT_DATA -o OUTPUT_DATA

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_DATA, --input_data INPUT_DATA
                            input data file.
    -o OUTPUT_DATA, --output_data OUTPUT_DATA
                            output preprocessed data.

Data Preparation 

    $ python prepare_data.py -h 
    usage: prepare_data.py [-h] -i INPUT_DATA -p PATH

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_DATA, --input_data INPUT_DATA
                            input data file.
    -p PATH, --path PATH  path for saving saving train and test data.

Model Training

    $ python train.py -h        
    usage: train.py [-h] -i INPUT_DATA -m MODEL_PATH

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_DATA, --input_data INPUT_DATA
                            input data file.
    -m MODEL_PATH, --model_path MODEL_PATH
                            path for saving trained model.

Model Evaluation

    $ python evaluate.py -h
    usage: evaluate.py [-h] -i INPUT_DATA -m MODEL_PATH

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_DATA, --input_data INPUT_DATA
                            input data file.
    -m MODEL_PATH, --model_path MODEL_PATH
                            path for loading the model.


# Use case
Load data file 

    $ python load_data.py -u http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv -p data/raw 
    #INFO: Data is succefully loaded!

Process data 

    $ python process_data.py -i data/raw/winequality-red.csv -o data/processed/winequality-red.csv
    #INFO: Data is succefully processed!

Prepare data 

    $ python prepare_data.py -i data/processed/winequality-red.csv -p data/prepared/
    #INFO: Data is succefully prepared!

Train the ML model

    $ python train.py -i data/prepared/train_winequality-red.csv -m models/elastic_net.pkl
    #INFO: Model is succefully trained!


Evaluate the model

    $ python evaluate.py -i data/prepared/test_winequality-red.csv -m models/elastic_net.pkl 
    #INFO:  RMSE: 0.7560270879287759
    #INFO:  MAE: 0.5986176396638518
    #INFO:  R2: 0.12714137617914456
    #INFO: Model is succefully evaluated!