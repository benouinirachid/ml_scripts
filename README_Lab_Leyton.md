# ml_scripts
Ready to use Machine Learning Python Scripts.

# Setup

Open the link

    https://colab.research.google.com/

Clone the repo 

    git clone https://github.com/benouinirachid/ml_scripts

    cd ml_scripts


Then you need to install the required python packages.

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

Model Scoring

    $ python predict.py -h
    usage: predict.py [-h] -f FEATURES -m MODEL_PATH

    optional arguments:
    -h, --help            show this help message and exit
    -f FEATURES, --features FEATURES
                            list of feeatures delimited by ',' .
    -m MODEL_PATH, --model_path MODEL_PATH
                            path for loading the model.


Model Evaluation

    $ python evaluate.py -h
    usage: evaluate.py [-h] -i INPUT_DATA -m MODEL_PATH

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT_DATA, --input_data INPUT_DATA
                            input data file.
    -m MODEL_PATH, --model_path MODEL_PATH
                            path for loading the model.


# Use case for boston housing price 
Load data file 

    !python load_data.py -u https://raw.githubusercontent.com/prachi1210/boston-housing-prices/master/housing.csv -p data/raw 
    #INFO: Data is succefully loaded!

Skip this step: Process data 

    !python process_data.py -i data/raw/housing.csv -o data/processed/housing.csv
    #INFO: Data is succefully processed!

Prepare data 

    !python prepare_data.py -i data/raw/housing.csv -p data/prepared/
    #INFO: Data is succefully prepared!

Train the ML model

    !python train.py -i data/prepared/train_housing.csv -t MDEV -m models/elastic_net_housing.pkl
    #INFO: Model is succefully trained!

Score the model on a new instance of data

    !python predict.py -f "6.012,12.43,15.2" -m models/elastic_net_housing.pkl
    the predicted value  is : 490283.1994

From the data we have, the following examples: 

Example 1

    Input (RM,LSTAT,PTRATIO): 6.012,12.43,15.2
    Target MDEV: 480900.0

Example 2

    Input (RM,LSTAT,PTRATIO): 6.674,11.98,21.0
    Target MDEV: 441000.0

Example 3

    Input (RM,LSTAT,PTRATIO): 5.856,25.41,19.1
    Target MDEV: 363300.0


Evaluate the model

    !python evaluate.py -i data/prepared/test_housing.csv -t MDEV -m models/elastic_net_housing.pkl 
    #INFO:  RMSE: 98337.63668750405
    #INFO:  MAE: 72492.53584397344
    #INFO:  R2: 0.6594985706877716
    #INFO: Model is succefully evaluated!