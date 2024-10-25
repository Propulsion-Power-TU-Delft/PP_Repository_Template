# PPTeam_Template Repository: Documentation

| Author  | E.C.Bunschoten  |
|------|------|
| Year  | 2024  |
| Group  | FPT  |
| Supervisors  | M.Pini,P.Colonna  |

# Documenting your code
Properly documenting your code is vital to its longevity and reproducebility of your results. Code documentation is different from code commenting! Comments in your code explain how specific parts of your code work, while the documentation describes how all components work together, as well as providing fundamental background knowledge on key functionalities. The documentation also allows you to demonstrate the code functionality through examples, making it easier for new users to get started using your code. 

Code documentation can be a tedious task, especially for large projects. In order to make it easier, we recommend to use available tools for automatic documentation. The documentation tool for this template repostitory is [Sphinx](https://www.sphinx-doc.org/en/master/index.html). Sphinx allows for automatically generating code documentation in LaTeX and html format. Visual Studio code supports auto docstring for Sphinx, which makes the process of properly documenting your code easy. 

## Getting started
In order to use Sphinx, you first need to install it. The [Sphinx website](https://www.sphinx-doc.org/en/master/usage/installation.html) gives you all the information you need in order to get it onto your system.

Once Sphinx has been installed, navigate to the folder where you'd like to compile the documentation and run the following command:

```
sphinx-quickstart
```

This will initiate the documentation set-up process. We recommend to generate separate source and build folders in order to keep things orderly. 
```
> Separate source and build directories (y/n) [n]: y
```
Name the project and set author name(s) and version accordingly. These can be changed later. Once the set-up is complete, two folders will be created: "build" and "source".

In order to generate the documentation for this repository, replace the ```documentation/source/conf.py``` file with ```documentation/conf_example.py``` and ```documentation/source/index.rst``` with ```documentation/index_example.rst```. Copy the files ```documentation/introduction.rst``` and ```documentation/examplefunction.rst``` to ```documentation/source/```.

Build the LaTeX documentation by running the command 

```
make latexpdf
```

The generated pdf can be found under ```documentation/build/latex/```. If instead you'd like to generate the documentation in html format, run the command

```
make html
```

The generated html can be found under ```documentation/build/html/``` named ```index.html``` and can be opened in your browser.