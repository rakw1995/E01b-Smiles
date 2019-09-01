# E01b-Smiles
This code is composed of 5 parts, each intended to produce different variations of a "smile" image, and are as follows: 
* Main1.py
    In main1.py, a smile should be created by changing the location values of each shape (x,y) to produce a smile image.
* Main2.py
    In main2.py, the code establishes a name for the coordinates (face x, face y)

* Main3.py
    In main3.py, the same smile should also be created, but this time it is centered as one complete object by defining the "center" and the location of other parts of the object in relation to that central point (face x, face y)
* Main4.py
    In main4.py, a repeating grid of the object should be created by assigning a loop to the values of x and y.

* Main5.py
In main5.py, the object should show up in the middle of the window until the mouse is moved, from which point it should follow the cursor movement by assigning values to three seperate functions:
    1. __init__ will define what the code needs to do initially (how big the window will be, the window title, background color, and the mouse cursor)
    2. on_draw will render the image according to the coordinates assigned
    3. on_mouse_motion will tell the computer that whatever coordinates the mouse is within the window, so too should the values of the self object be