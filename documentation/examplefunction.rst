Example function
================

.. raw:: html 

    You can write your documentation in html. This makes it easy to publish your documentation via a website and generates a nice search bar which makes it easy to scan through your code. 
    Within the scope of ..raw:: html, you can write any text in html format. 
    Documentation of functions is made easier with the ..autofunction:: functionality. As long as you use the Sphinx docstring format in your code, and the 
    code is present on your environment path (PYTHONPATH in this example), Sphinx will automatically compile the documentation for your functions.

    The first function writes input data for training a multi-layer perceptron (MLP). 

.. raw:: latex 


    You can also write it in LateX. Within the scope of .. raw:: latex, you can write in LateX format using all the packages, environments, and variables you define under the preamble in conf.py
    Be careful, the .. raw:: latex scope is sensitive to indices and empty lines! 

    Documentation of functions is made easier with the ..autofunction:: functionality. As long as you use the Sphinx docstring format in your code, and the 
    code is present on your environment path (PYTHONPATH in this example), Sphinx will automatically compile the documentation for your functions.

    The first function writes input data for training a multi-layer perceptron (MLP). 


.. autofunction:: MLP_functions.write_input_data 

.. raw:: html 


    The second function scales the training data based on standard deviation. 


.. raw:: latex 


    The second function scales the training data based on standard deviation. 


.. autofunction:: MLP_functions.scale_input_data


.. raw:: html


    The final function here generates a TensorFlow model ready for training.


.. raw:: latex 


    The final function here generates a \texttt{TensorFlow} model ready for training.


.. autofunction:: MLP_functions.define_tensorflow_model