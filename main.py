from exceptions import NegativeLenghtError, NotAllowedNumberError, TriangleDoesnotExistError, WrongInput

from random import randint as rand
from exceptions import IncorrectNumberType, NumberIsTooLargeError

class Triangle:
    """
    Simple class for triangle types.
    Prints out what type the triangle is.
    """
    
    _sides_names = ("A", "B", "C")
    
    def __init__(self, sides_lenghts: list[int]) -> None:
        
        for i, _ in enumerate(sides_lenghts):
            if not isinstance(sides_lenghts[i], (int, float)):
                raise NotAllowedNumberError(self._sides_names[i], sides_lenghts[i])
            elif sides_lenghts[i] <= 0:
                raise NegativeLenghtError(self._sides_names[i], sides_lenghts[i])
            elif len(sides_lenghts) != 3:
                raise WrongInput("lengthW")
            
        for x in sides_lenghts:
            sides_lenghts.remove(x)
            cat_1, cat_2 = sides_lenghts
            if x > cat_1 + cat_2:
                raise TriangleDoesnotExistError(x, cat_1, cat_2)
            sides_lenghts.append(x)
        
        x = sides_lenghts[-1]
        sides_lenghts.pop(-1)
        sides_lenghts = sides_lenghts[::-1]
        sides_lenghts.append(x)
        
        self._side_lenghts = sides_lenghts
        
    def check_triangle(self) -> str:
        arr_set = set(self._side_lenghts)

        if len(arr_set) == 2:
            print("Triangle is an isosceles triangle")
        elif len(arr_set) == 1:
            print("Triangle is a equilateral Triangle")
        else:
            print("Triangle is a scalene triangle")        
    
    def __str__(self) -> str:
        self.check_triangle()
        s = ""
        for i, _ in enumerate(self._side_lenghts):
            s += f"Side {self._sides_names[i]} : {self._side_lenghts[i]}\n"
        return s


class PrimeTest:
    """
    Class that checks if a number is a prime or not.
    """
    _MAX_NUMBER = 100_000_000
    _MIN_NUMBER = -100_000_000
    
    def __init__(self, num: int) -> None:
        if not isinstance(num, int):
            raise IncorrectNumberType("Integer", num)
        self.num = num
        if not self.allowed_number():
            raise NumberIsTooLargeError(self.num, self._MIN_NUMBER, self._MAX_NUMBER)
        
    def even_or_odd(self) -> bool:
        return True if int(self.d) % 2 == 0 else False
    
    def allowed_number(self) -> bool:
        return True if self.num < self._MAX_NUMBER and self.num > self._MIN_NUMBER else False
    
    # We will use Miller–Rabin test. Assume that zero is a prime.    
    def test(self) -> bool:
        """Using Miller-Rabin test we will find out if num is a prime.
        Returns:
            True if entered number is a prime.
            False if not a prime.
        """
        self.d: float = self.num - 1
        s, a = 0, 0
        x, y = 0.0, 0.0
        
        while self.even_or_odd():
            s += 1
            self.d /= 2
            
        for i in range(0, 25):
            a = rand(2, self.num - 2)
            x = (a ** self.d) % self.num
            for j in range(s + 2):
                y = (x ** 2) % self.num
                if y == 1 and x != 1 and x != self.num - 1:
                    return False
                x = y
        return True
    
    def __str__(self) -> str:
        return f"Entered number {self.num} is a prime." if self.test() else f"Entered number {self.num} is not a prime."


class Game:
    def __init__(self, guees_amount: int = None, range: list[int] = None) -> None:
        self.num: int = 0
        
        if range is None:
            range = [0, 1000 + 1]        
                
        self.secret_number = rand(*range)
        
        if guees_amount is None:
            guees_amount = 10

        self.guees_amount = guees_amount
        
    def clues(self) -> bool:
        if self.num == self.secret_number:
            return True
        elif self.num > self.secret_number:
            print(f"The number is smaller than:\n{self.num}")
        else:
            print(f"The number is bigger than:\n{self.num}")
        return False
    
    def mainloop(self):
        print("Program is working.\n"
            "I came up with a number try to guess it.\n"
          f"You have {self.guees_amount} tries to do it.")
        for i in range(self.guees_amount, 0, -1):
            try:
                self.num = int(input())
            except Exception as e:
                raise IncorrectNumberType("Integer", self.num)
            if self.num not in range(0, 1000 + 1):
                raise NumberIsTooLargeError(self.num, 0, 1000)
            
            if self.clues():
                print("Correct")
                break
            else:
                print(f"Wrong.\nTry again you have {i} tries left")
        else:
            print(f"The number was {self.secret_number}")


if __name__ == "__main__":
    triangle = Triangle([3, 4, 5])
    print(triangle)
    num = PrimeTest(251)
    print(num)
    game = Game(10)
    game.mainloop()
    