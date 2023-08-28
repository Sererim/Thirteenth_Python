class UserException(Exception):
    pass


class NegativeLenghtError(UserException):
    def __init__(self, side_name: str, side_length: int) -> None:
        self.name = side_name
        self.num = side_length
    
    def __str__(self) -> str:
        return f"Side {self.name} with length {self.num} can not exist.\nPlease enter only positive numbers."


class NotAllowedNumberError(UserException):
    
    def __init__(self, name, value) -> None:
        self.value = value
        self.name = name
    
    def __str__(self) -> str:
        return f"Side {self.name} with value {self.value} is of {type(self.value)}, that is not allowed. Only 'int' or 'float' are allowed values."


class TriangleDoesnotExistError(UserException):
    def __init__(self, *args) -> None:
        self.args = args
    
    def __str__(self) -> str:
        return f"{self.args[0]} > {self.args[1]} + {self.args[-1]}"


class WrongInput(UserException):
    
    def __init__(self, error: str) -> None:
        self.error = error
        
    def __str__(self) -> str:
        return f"Wrong input. Such {self.error} is not allowed."


class IncorrectNumberType(UserException):
    def __init__(self, name, num) -> None:
        self.num = num
        self.type = name
        
    def __str__(self) -> str:
        return f"{self.num} of type {type(self.num)}\nIs not allowed. Only {self.type} is allowed."


class NumberIsTooLargeError(UserException):
    def __init__(self, value: int, MIN: int, MAX: int) -> None:
        self.value = value
        self.MIN = MIN
        self.MAX = MAX
        
    def __str__(self) -> str:
        return f"Entered number {self.value} is not within the range of [{self.MIN}, {self.MAX}]"

