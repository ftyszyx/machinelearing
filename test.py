# import tensorflow as tf
# classifer=tf.estimator.LinearClassfier()
# classifer.train(input_fu=train_input_fn,steps=2000)
# predictions=classifer.predict(input_fu=predict_input_fn)
import numpy as np
import pandas as pd 
dateset=pd.read_csv("Data.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc
