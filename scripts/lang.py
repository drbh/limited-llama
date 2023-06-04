import random

class Element:
    def __init__(self, value):
        self.value = value

class Set:
    def __init__(self, elements):
        self.elements = [Element(i) for i in elements]

    def __sub__(self, other):
        self.elements = [e for e in self.elements if e != other]
        return self

class Operation:
    def execute(self):
        raise NotImplementedError

class Subtract(Operation):
    def __init__(self, element1, element2):
        self.element1 = element1
        self.element2 = element2

    def execute(self):
        return Element(self.element1.value - self.element2.value)

class OneOf(Operation):
    def __init__(self, set):
        self.set = set

    def execute(self):
        if len(self.set.elements) == 0:
            raise ValueError('Set is empty')
        chosen_element = random.choice(self.set.elements)
        self.set = self.set - chosen_element
        return chosen_element


# Simple API for a lazy executed set operation language
original = Set([1,2,3,4]) 
first_option = OneOf(original).execute() 
original = original - first_option
second_option = OneOf(original).execute() 
compute_result = Subtract(second_option, first_option) 

compute_output = compute_result.execute() 
print(compute_output.value)
