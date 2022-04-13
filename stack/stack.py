import abc
from tkinter import W

class ADTStack(abc.ABC):
   @abc.abstractmethod
   def push(self, e):
       """Add element e to the top of the stack."""
       pass
   
   @abc.abstractmethod
   def pop(self): 
       """Remove and return the element from the top of the stack.
        
        Raise
            EmptyStack if stack is empty.
        """
       pass
   
   @abc.abstractmethod
   def top(self): 
       """Return top element of the stack without removing it.
       
        Raise
            EmptyStack if stack is empty.
        """
       pass
   
   @abc.abstractmethod
   def is_empty(self): 
       """Return True if the stack is empty."""
       pass
   
   @abc.abstractmethod
   def __len__(self): 
       """Return the number of elements in the stack."""
       pass

class EmptyStack(Exception):
    """Exception to raise when a stack is empty."""
    pass

class Stack(ADTStack):
    def __init__(self):
        self._data = []
    
    def push(self, e):
        self._data.append(e)
        
    def pop(self):
        if self.is_empty():
            raise EmptyStack("No element to pop")
        return self._data.pop()
    
    def top(self):
        if self.is_empty():
            raise EmptyStack("No element on top")
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)