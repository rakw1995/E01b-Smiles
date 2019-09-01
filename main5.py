#!/usr/bin/env python3 #this is the file location

import utils, open_color, arcade #this imports the resources needed for the code to work

utils.check_version((3,7)) #this verifies you are using the correct version of python

SCREEN_WIDTH = 800 #the window will be 800px in width
SCREEN_HEIGHT = 600 #the window will be 600px in height
SCREEN_TITLE = "Smiley Face Example" #the title in quotations will appear in the window's title line

class Faces(arcade.Window): #this defines the class
    """ Our custom Window Class""" #this describes the previous line
#this section within the class initializes the window and all of its values
    def __init__(self): #this defines where all values attributed to self START.
        """ Initializer """ #this describes the previous line
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #this prevents you from having to repeat the code for these values (it binds these values to the initializer)

        self.set_mouse_visible(True) # Show the mouse cursor when it is within the window

        self.x = SCREEN_WIDTH / 2 #this is where the object will start before the mouse moves, or "width" divided by 2
        self.y = SCREEN_HEIGHT / 2 #this is where the object will start before the mouse moves, or "height" divided by 2

        arcade.set_background_color(open_color.white) #the background within the window will be white
#this section renders the drawing
    def on_draw(self): #this tells the computer "draw" the face
        """ Draw the face """ #description of what the previous line should do
        arcade.start_render() #this tag is required for the code to begin
        face_x,face_y = (self.x,self.y) #this attributes the x and y values for the "face" to the "self" object(what is attributed to self, face will do)
        smile_x,smile_y = (face_x + 0,face_y - 10) #the smile will be offset from the "face" by 0, -10.
        eye1_x,eye1_y = (face_x - 30,face_y + 20) #eye1 will be offset by -30,20
        eye2_x,eye2_y = (face_x + 30,face_y + 20) #eye2 will be offset by 30,20
        catch1_x,catch1_y = (face_x - 25,face_y + 25) #catch1 will be offset by -25,25
        catch2_x,catch2_y = (face_x + 35,face_y + 25) #catch2 will be offset by 35,25

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #this creates a yellow circle that is 100px in radius
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #this creates a black outline that is 100px in radius
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black) #this creates a black, filled ellipse that is 15x25px
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)#this creates another black, filled ellipse that is 15x25px
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2) #this creates a gray highlight that is 3px
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2) #this creates another gray highlight that is 3px
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4) #this creates an outline in black that is used to create the smile (60widthx50height,190 is the starting degree of the angle, 350 is the ending degree of the angle. The line is 4px thick.)

#this section relates to mouse motion
    def on_mouse_motion(self, x, y, dx, dy): #when the mouse moves, this tells the computer to move all objects that are attributed to what is in the parenthesis. 
        """ Handle Mouse Motion """ #this explains to the user what the previous line is for
        self.x = x #this attributes the self values of x to the mouse location in the window
        self.y = y #this attributes the self values of y to the mouse location in the window


window = Faces() #this is the ending for the Faces class and all values attributed to it
arcade.run() #this runs the program until it is manually closed