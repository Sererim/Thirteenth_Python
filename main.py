from exceptions import NegativeLenghtError, NotAllowedNumberError, TriangleDoesnotExistError, WrongInput

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


if __name__ == "__main__":
    triangle = Triangle([3, 4, 5])
    print(triangle)
    