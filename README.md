# PPTeam_Template Repository

| Author  | E.C.Bunschoten  |
|------|------|
| Year  | 2024  |
| Group  | FPT  |
| Supervisors  | M.Pini,P.Colonna  |

## Summary

This template repository was made for Master students and PhD candidates in order to facilitate sustainable, shared, and transparent software development for research purposes. You can copy this repository and use it during your research in order to keep your code consistent between devices, easy to share, and secure. While writing code, follow the guidelines in this repository in order to keep your code readable and therefore easy to use and develop further. At the end of your thesis, make sure you have checked all the boxes in the last section of this document.

In this section, give a short summary of your work. It can be a summary of your thesis work for example. If so, make sure you give links to relevant literature (such as your thesis). Here is a [link](https://www.markdownguide.org/cheat-sheet/) to some general tips on writing in markdown format. 

TODO: Add some information regarding collaborative code development using git here.


## Related work and contributions

Is your code based on or uses code from other repositories? Make sure you list those works here. Highlight what you have improved and/or changed with respect to those fundamental works. What are neat things you can do with the code in this repository and how are they related to scientific development? 


## Set-up

This section describes how to set-up the software in your repository so it can be used by others on their own hardware. Give a clear, step-by-step explanation on how to get the code onto your system, compile, and use your code. Fill in the sections on hardware and software requirements in order to communicate which software versions you were using while developing this code. Below are some examples of what you may want to list there.

### Hardware requirements
- Operating system: Ubuntu 22.04
- Memory: 8 GB
- Storage: - 
- NVIDIA GPU

### Software requirements 
- Python v. 3.11
- Matlab 2024b
- Paraview 5.11

Also list packages that are required for running your software. For example, which python modules and versions are used by your code? Do you need any specific Matlab toolboxes? 

### Python modules
- numpy - 1.26.4
- matplotlib - 3.9.0
- tensorflow -2.16.1

### Installation 
List the installation instructions that you need to perform in order to get your code working on new users' hardware. In order to run the examples for this repository, clone the repository onto your system:

```
git clone https://github.com/EvertBunschoten/PPTeam_Template <install dir>
```
where ```<install dir>``` is the target directory where you want to download the code.

Finally, add the following line to your ```.bashrc``` in order to expose the python functions in this repository to your python interpreter.

```
export $PYTHONPATH=PYTHONPATH:<install dir>/src/src_python
```


## Repository structure

In this section, give a brief outline of your repository structure. Which folder contains what? If a new developer would like to add something like a test case or a new module, where would they need to add it? 

## Graduation checklist

To make sure your repository is set up correctly, complete the tasks below:
- [ ] My repository has a description.
- [ ] The README has all the information for summary, related work, set-up, and structure.
- [ ] My source code is sufficiently commented.
- [ ] I have added at least one tutorial that explains in steps how to use my software.
- [ ] I have added at least one test case that is discussed in my thesis if applicable.
- [ ] I have added at least one regression test that checks the integrity of my software.
- [ ] I have added basic documentation on my software that explains more details on the implementation.
- [ ] I have had at least one peer check out my code and run the regression tests on their own hardware.

