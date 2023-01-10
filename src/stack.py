class Stack:
    def __init__(self):
        self.__elements = []

    def is_empty(self):
        return self.__elements == []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        return self.__elements.pop()

    def peek(self):
        return self.__elements[len(self.__elements)-1]

    def size(self):
        return len(self.__elements)
