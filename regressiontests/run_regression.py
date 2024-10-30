#!/usr/bin/env python3

"""
File name: run_regression.py
Author: E.C.Bunschoten
Year: 2024

Summary: This file can be used as a template for automatically running regression tests. You can use this 
to make sure nothing in your code breaks when adding new functionalities. For every key functionality of 
your code, add a regression test. Make sure the regression tests pass on your hardware before pushing 
new commits.
"""

# Import relevant modules 
import sys 
from TestCase import TestCase 

def main():
    
    test_list:list[TestCase] = [] 

    # Below you can define a set of test cases that check your code consistency and performance.
    # Simple MLP training

    # Name your test case. This name will appear in the terminal when running the regression test.
    simpleMLP = TestCase("SimpleMLP")   

    # Set regression test directory relative to the directory of this script.
    simpleMLP.regression_test_dir = "../testcases/testcase_1/"

    # Define arguments to your regression test.
    simpleMLP.command_line_arguments = ""

    # Terminal command needed to run your regression test without arguments.
    simpleMLP.exec_command = "python3 train_simple_MLP.py"

    # List a set of files of which the content is compared to what the regression test produces.
    simpleMLP.reference_files = ["test_data_ref.csv"]

    # List the set of files of which the content is compared to that of the reference files.
    simpleMLP.test_files = ["test_data.csv"]

    test_list.append(simpleMLP)

    # Add more regression tests ...

    
    # Run all regression tests in regression test list.
    pass_list = [test.run_test() for test in test_list]

    # Tests summary
    print('==================================================================')
    print('Summary of the serial tests')
    print('python version:', sys.version)
    for i, test in enumerate(test_list):
        if (pass_list[i]):
            print('  passed - %s'%test.tag)
        else:
            print('* FAILED - %s'%test.tag)

    if all(pass_list):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
