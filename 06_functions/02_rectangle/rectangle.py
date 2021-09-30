def area(width, height):
    """The functions return the area of the rectangle"""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The widht and height must be of type int or float')

    if not (width > 0 and height >0):
        raise ValueError('The width and height must be positive.')

    return width * height


def perimeter(width, height):
    """The function returs of perimeter of the rectangle"""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The widht and height must be of type int or float')

    if not (width > 0 and height >0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height