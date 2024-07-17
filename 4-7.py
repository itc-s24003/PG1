def make_circle_area_func(pi = 3.14): 
    def circle_area(radius): 
        return radius * radius * pi 
    return circle_area 
circle_area_default = make_circle_area_func() 
circle_area_precise = make_circle_area_func (pi = 3.1415926535) 

