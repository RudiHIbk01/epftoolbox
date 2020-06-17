from epftoolbox.dnn.recalibration_and_forecasting import evaluate_model_in_test_dataset


# Number of layers in DNN
nlayers = 2

# Market under study. If it not one of the standard ones, the file name
# has to be provided, where the file has to be a csv file
dataset = 'PJM'

# Number of years (a year is 364 days) in the test dataset.
years_test = 2

# Boolean that selects whether the validation and training datasets are shuffled
shuffle_train = 1

# Boolean that selects whether a data augmentation technique for DNNs is used
data_augmentation = 0

# Boolean that selects whether we start a new recalibration or we restart an existing one
new_recalibration = 1

# Number of years used in the training dataset for recalibration
calibration_window = 4

# Unique identifier to read the trials file of hyperparameter optimization
experiment_id = 1

# Optional parameters for selecting the test dataset, if either of them is not provided, 
# the test dataset is built using the years_test parameter. They should either be one of
# the date formats existing in python or a string with the following format
# "%d/%m/%Y %H:%M"
begin_test_date = None
end_test_date = None

path_datasets = "./datasets/"
path_recalibration_files = "./experimental_files/"
path_hyperparameter_files = "./experimental_files/"
    
evaluate_model_in_test_dataset(experiment_id, hyperparameter_files=path_hyperparameter_files, 
                               path_datasets=path_datasets, shuffle_train=shuffle_train, 
                               path_recalibration_files=path_recalibration_files, 
                               nlayers=nlayers, dataset=dataset, years_test=years_test, 
                               data_augmentation=data_augmentation, calibration_window=calibration_window, 
                               new_recalibration=new_recalibration, begin_test_date=begin_test_date, 
                               end_test_date=end_test_date)