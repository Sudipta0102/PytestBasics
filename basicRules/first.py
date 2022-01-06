# 1. you need to import pytest
import pytest
# 2. need to have the file name with test_*.py or *_test.py
# 3. need to have function name with test_*()

def func1():
    name = 'nonproblem'
    print(f"i am {name}")

if __name__=='__main__':
    func1()


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
# i think be used as groups in TestNG


#-------------------------------------------------------------------------------------------------------

# Markers:
# as I can understand markers can be used as
