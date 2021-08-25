"""
Processing Demo
"""

# Processing has many built in functions to draw colorful
# shapes very easily. Lets do a quick example:
def setup():
    # The size(width, height) function creates a window with
    # the specified with and height 
    size(500, 600)


def draw():
    # background() draws the color or image onto the window.
    # In this case the '#FFFFFF' is white
    background('#B9F4FF')
    
    # fill() sets the color. In this case, it's Blue
    # You can create custom colors using Tools->Color Selector
    fill('#71B785')

    # ellipse() draws an ellipse that follows the mouse position
    # (mouseX and mouseY) with the following inputs:
    #         x,      y,   width, height
    ellipse( 250, 200, 80,50)
    
    rect(300,250, 70, 100)
    # The code below checks of the mouse was pressed and draws
    # a red ellipse over the blue one
    if mousePressed:
        fill('#FF0000') 
        ellipse(mouseX, mouseY,  90,   100)
        
    

    # TODO: Add some other shapes with different sizes and colors
    # rect(x, y, width, height)
    # triangle(x1, y1, x2, y2, x3, y3)
    
