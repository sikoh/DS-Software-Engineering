### IN style_example.py FILE###

#what would you say if you were working with someone and this is the code they gave you?

import math, sys

def exampl1():
    '''This is a long comment and should be wrapped
     to fit within a 72 character limit'''

    string1 = '''LONG CODE LINES should be wrapped within 79
                    character to prevent page cutoff stuff'''
    string2 = '''This is a long string that looks 
                gross and goes beyond what it should'''

    some_tuple = (1,2, 3, 'a')
    some_variable = {"long":string1,
                    "other":[math.pi, 100,200, 300, 9999292929292,string2],
                    "more": {"inner": "THIS whole logical line should be wrapped"},
                    "data": [444,5555,222,3,3,4,4,5,5,5,5,5,5,5]}
    result = (some_tuple, some_variable)

    return result

def example_2(): 
    result = {"has_key() is deprecated": True}
    return result
    
class Example3(object):
    def __init__(self, bar):
        bar+= 1
        bar=bar* bar
        print(bar)
        some_string = """Indentation in multiple strings 
                    should not be touched only actual code 
                    should be reindented, this is more code"""
        return (sys.path, some_string)
