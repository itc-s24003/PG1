def show_how_is_works(func):
  def my_function(*args, **kwargs):
    print('Running function:', func.__name__)
    print('Positional arguments:', args)
    print('Keyword arguments:', kwargs)
    result = func(*args, **kwargs)
    print('Result:', result)
    return result
  return my_function

@show_how_is_works
def add_two_numbers(a, b):
  return a + b

#decodated_fuc = show_how_is_works(add_two_numbers)
#decodated_fuc(1, 8)

#add_two_numbers(1, 8)

