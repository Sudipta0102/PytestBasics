# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 1. you need to import pytest
import pytest
# 2. need to have the file name with test_*.py or *_test.py
# 3. need to have function name with test_*()


# question 1.:
# how do you run one test file from multiple test file?
# what you need to do is,
# 1. get to the path where the file resides
# 2. run pytest fllename
# from anywhere, give that filepath with pytest or py.test


# question 2:
# how do you run a single function?
# pytest -k: where -k denotes expression
# you can pass an expression consists of your filename here. What it will do is, in that path,
# if you have any test named after the keyword that you provided. It will run. like this,
# pytest -k func1 -v (-v is for verbosity)


# -------------------------------------------------------------------------------------------------------

# Markers:

# Custom->

# 1. as I can understand markers can be used as groups to define SANITY, SMOKE, REGRESSION etc. or
# you can group tests as per their functionality or any way you like
# 2. it has a decorator like this.
# @pytest.mark.REGRESSION (this last part is user defined)
# 3. to run multiple markers at a time use pytest -m "USER and SMOKE" -v
# It also will work with more complex expressions like 'a and b or c' etc etc
# 4. When running, i get this:
# PytestUnknownMarkWarning: Unknown pytest.mark.REGRESSION - is this a typo?  You can register custom marks to avoid
# this warning
# this is because the markers is not registered yet.
#       a. To register, you need to have a file called pytest.ini (a configuration file) in my
#       root directory to register the markers I am using.
#       b. mention all the custom markers under 'markers' key.
#       c. I also have an option where I can restrict my test execution only to the registered markers.
#       These are called Strict Markers. usage of unregistered markers will lead to errors.
#        Way to achieve this is,
#           addopts = --strict-markers
#
#
#
# Built in ->
#
# 1. @pytest.mark.skip -> skips a test
# 2. @pytest.mark.xfail -> When a test is marked as ‘xfail’, the test is executed but whether
# it passes or fails does not affect the overall result fo the test.
# in th real world, this marker can be used is TDD when some functionality is not yet implemented
# by the developer.
#
#
# -------------------------------------------------------------------------------------------------------
# Parallel Mode execution:
# 1. need to install xdist plugin by running command -> pip install pytest-xdist
# 2. Write your test but when running run this command -> pytest -n 4 test_name.py -v
# here, 4 is thread count.
# Now I understand this is the most basic things in this package and I got to know that
# there is one another package called "pytest-parallel" is used for same purpose.
# Follow up: Check both of them, locate the pros and cons.
#
#
# -------------------------------------------------------------------------------------------------------
#
# Fixtures:
# 1. classic xunit-style setup: this can be done in three levels
#   a. Module level : If you have like multiple test functions or test classes in a single module then,
# then this fixture can be optionally implemented which will be called once for all the functions.
#
#   b. class level:
#   c. method level:
#   d. function level:
#
#
#
#
# 2. fixture decorator:
#   a. this looks like pytest.fixture -> there are bunch of args can be used, most notably 'scope'
#   b. this is used to set the preconditions and postconditions of test suite. (this is only one aspect of that)
#   c. generally speaking you can any context for you test suite like database loading or log initialization etc
#   d. when it comes to setup/teardown, it does the same thing on every level as xunit-style setup does, but better.
# details: https://docs.pytest.org/en/latest/explanation/fixtures.html
#           header: Improvements over xUnit-style setup/teardown functions
#
# Note: there are many tihngs here to learn and apply, will need to come back
#
#
# -------------------------------------------------------------------------------------------------------
# Html report:
# 1. run: pip install pytest html
# 2. to run the test -> pytest .\module_level.py -v -s --html=report_name.html

