
# Import modules and set seed values for reproducability.
seed_value = 2
import os
os.environ['PYTHONASHSEED'] = str(seed_value)
seed_value += 1
import random
random.seed(seed_value)
seed_value += 1
import numpy as np
np.random.seed(seed_value)
seed_value += 1 
import tensorflow as tf
tf.random.set_seed(seed_value)
from sklearn.preprocessing import StandardScaler

def write_input_data(Np:int=5000, f:float=1.0):
    """Generate training data.

    :param Np: number of data points, defaults to 5000
    :type Np: int, optional
    :param f: factor for contribution of second controlling variable, defaults to 1.0
    :type f: float, optional
    """

    t = np.linspace(0, 1, Np)
    u = (1 - t) * np.cos(48*np.pi*t)
    v = (1 - t) * np.sin(48*np.pi*t)

    y = np.sin(2*np.pi*(u*u + f*v))
    return u, v, y

def scale_input_data(X_dim_in:np.ndarray[float], Y_dim_in:np.ndarray[float],\
                     scaler_function_x:StandardScaler, scaler_function_y:StandardScaler):
    """Normalize the input and labeled data.

    :param X_dim_in: dimensional controlling variable input data.
    :type X_dim_in: np.ndarray[float]
    :param Y_dim_in: dimensional labeled input data.
    :type Y_dim_in: np.ndarray[float]
    :param scaler_function_x: scaler function used to normalize controlling variable data.
    :type scaler_function_x: StandardScaler
    :param scaler_function_y: scaler function used to normalize labeled data.
    :type scaler_function_y: StandardScaler
    :raises Exception: if number of data points between labeled and controlling variable data differs.
    :return: normalized controlling variable data and normalized labeled data arrays
    :rtype: np.ndarray[float]
    """
    if np.shape(X_dim_in)[0] != np.shape(Y_dim_in)[0]:
        raise Exception("Number of data points for controlling variables and labeled data should be the same.")
    
    scaler_function_x.fit(X_dim_in)
    scaler_function_y.fit(Y_dim_in)

    X_norm = scaler_function_x.transform(X_dim_in)
    Y_norm = scaler_function_y.transform(Y_dim_in)
    return X_norm, Y_norm

def define_tensorflow_model(hidden_layers:list[int]=[10,10,10],lr_init:float=1e-2, lr_decay:float=0.99):
    """Set up a dense, feed forward MLP using the keras sequential model.

    :param hidden_layers: hidden layer neuron architecture, defaults to [10,10,10]
    :type hidden_layers: list[int], optional
    :param lr_init: initial learning rate, defaults to 1e-2
    :type lr_init: float, optional
    :param lr_decay: learning rate decay parameter for exponential decay schedule, defaults to 0.99
    :type lr_decay: float, optional
    :raises Exception: if any of the hidden layers contains fewer than two neurons.
    :raises Exception: if no hidden layer architecture is provided.
    :return: compiled model ready for training.
    :rtype: tf.keras.models.Sequential
    """

    if any([n < 2 for n in hidden_layers]):
        raise Exception("Number of perceptrons should be higher than 2")
    if len(hidden_layers) == 0:
        raise Exception("At least one hidden layer should be defined.")
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Input([2]))
    for NN in hidden_layers:
        model.add(tf.keras.layers.Dense(NN,activation='sigmoid',kernel_initializer="he_uniform"))
    model.add(tf.keras.layers.Dense(1, activation='linear'))

    # Set up training method
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(lr_init, decay_steps=1000,decay_rate=lr_decay,staircase=False)
    opt = tf.keras.optimizers.Adam(learning_rate=lr_schedule,beta_1=0.9,beta_2=0.999,epsilon=1e-08,amsgrad=False)

    # Commence training
    model.compile(optimizer=opt,loss="mean_squared_error",metrics=["mape"])
    return model 
