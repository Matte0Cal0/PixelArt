import turtle

#Turtle Settings
TURTLE_SIZE = 20
SQUARE_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'normal')
size:int=32

#Color Palette 
colors:list=[[255,255,255], #white
            [193,193,193], #lightgray
            [255,0,0], #red
            [255,113,0], #orange
            [255,228,0], #yellow
            [0,204,0], #green
            [0,178,255], #lightblue
            [35,31,211], #blue
            [163,0,186], #purple
            [211,124,170], #pink
            [160,82,45], #brown
          
            [0,0,0], #black
            [76,76,76], #darkgrey
            [116,11,7], #darkred
            [194,56,0], #darkorange
            [232,162,0], #darkyellow
            [0,85,16], #darkgreen
            [0,86,158], #darklightblue
            [14,8,101], #darkblue
            [85,0,105], #darkpurple
            [167,85,116], #darkpink
            [99,48,13]] #darkbrown

#Default color at launch is White
selectedColor = [255,255,255]

#Get the selected color
def getSelectedColor():
    return selectedColor

#Set the selected color
def setSelectedColor(color:list):
    global selectedColor
    selectedColor = color

#Get the Hexadecimal value of the color
def getHex(pixel:list):
    return "#{:02x}{:02x}{:02x}".format(pixel[0],pixel[1],pixel[2])

#On click function
def toggle(pixel, selectedColor):
    """Toggles the colour of a Turtle when it is clicked."""
    pixel.color(getHex(selectedColor))

#Select the color
def selectColor(color):
    setSelectedColor(color)
    print("Selected color: " + getHex(selectedColor))

#Screen Setup
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title("Pixel Art")
screen.bgcolor(getHex([100,100,100]))

#Disable Animation
screen.tracer(0)

#Initialize White Grid
def initGrid(size:int):
    liste:list=[]
    for i in range(size):
        liste.append([])
        for j in range(size):
            liste[i].append([255,255,255])
            
    return liste

grid:list=initGrid(size)
          
#Initialize Color Palette
def turtleInitPalette(grid:list):
        for i in range(2):
            for j in range(11):
                pixel = turtle.Turtle("square")
                
                offsetx = -130
                offsety = -410

                color = colors[i*11 + j]
                
                def click_callback(x, y, color=color):
                    """Passes `pixel` to `toggle()` function."""
                    return selectColor(color)
                
                pixel.shapesize(SQUARE_SIZE / TURTLE_SIZE)
                pixel.color(getHex(color))
                pixel.penup()
                pixel.goto(offsetx + j * (SQUARE_SIZE + 2), 0 + offsety + i * (SQUARE_SIZE + 2))
                pixel.onclick(click_callback)
              
#Initialize Pixel Grid              
def turtleInitGrid(grid:list):
    for i in range (0,len(grid)):
        for j in range (0,len(grid)):
            pixel = turtle.Turtle("square")
            offset = -350
            
            def click_callback(x, y, pixel=pixel):
                """Passes `pixel` to `toggle()` function."""
                return toggle(pixel, selectedColor)
            
            pixel.shapesize(SQUARE_SIZE / TURTLE_SIZE)
            color = grid[i][j]
            pixel.color(getHex(color))
            pixel.penup()
            pixel.goto(offset + j * (SQUARE_SIZE + 2), 0 + offset + i * (SQUARE_SIZE + 2))
            pixel.onclick(click_callback)
            screen.tracer(0)
            
#Reset function
def reset():
    screen.tracer(0)
    turtleInitPalette(grid)
    turtleInitButtonReset(grid)
    turtleInitGrid(grid)
    screen.tracer(1)
    
    
#Initialize Reset Button
def turtleInitButtonReset(grid:list):
        pixel = turtle.Turtle("square")
        SQUARE_SIZE = 40
        offset = -400
        
        def click_callback(x, y, pixel=pixel):
            """Passes `pixel` to `toggle()` function."""
            reset()
            
        pixel.shapesize(SQUARE_SIZE / TURTLE_SIZE)
        pixel.color("red")
        pixel.penup()
        pixel.goto(offset + 0* (SQUARE_SIZE + 2), 0 + offset + 2 * (SQUARE_SIZE + 2))
        pixel.onclick(click_callback)
        
        #Reset Text
        pen = turtle.Turtle(visible=False)
        pen.color("black")
        pen.penup()
        pen.goto(offset + 0* (SQUARE_SIZE + 2), 0 + offset + 3 * (SQUARE_SIZE + 2))
        pen.write("Reset", align="center", font=FONT)
        pen.forward(22)

#Initialization of the tool
turtleInitPalette(grid)
turtleInitButtonReset(grid)
turtleInitGrid(grid)

#Restore animation
screen.tracer(1)

#End Turtle
turtle.done()
