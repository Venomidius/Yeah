material = '*'
space = ' '
height = 12
border_width = 2
if height / border_width >= 2:
    for top in range(border_width):
        top_space = (height - top - 1) * space
        top_material = (2 * top + 1) * material
        top = top_space + top_material
        print(top)
    for middle in range(border_width, height - border_width):
        middle_left_space = (height - middle - 1) * space
        middle_middle_space = (2 * (middle - border_width) + 1) * space
        middle_material = border_width * material
        middle = middle_left_space + middle_material + middle_middle_space + middle_material
        print(middle)
    for bottom in range(border_width):
        bottom_space = (border_width - bottom - 1) * space
        bottom_material = (((2 * border_width) + (2 * (height - (2 * border_width)) + 1)) + (2 * bottom)) * material
        bottom = bottom_space + bottom_material
        print(bottom)