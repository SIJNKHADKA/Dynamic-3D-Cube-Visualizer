import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

vertices = ( 
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1),
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),

)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
)

def set_vertices(max_distance,min_distance = -20, camera_x = 0, camera_y = 0):
    camera_x = -1 * int(camera_x)
    camera_y = -1 * int(camera_y)

    x_value_change = random.randrange(camera_x-35,camera_x +35)
    y_value_change = random.randrange(camera_y-35,camera_y +35)
    z_value_change = random.randrange(-1*max_distance,min_distance)

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

def cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x +=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()
def main():

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
#uses two arguments : display and flags(modify the behavior and properties of the display
    max_distance = 100
    gluPerspective(45,(display[0]/display[1]),0.1,max_distance)
#setup perspective projection matrix: transfer 3D coordinates into 2D

    glTranslatef(0,0,-40)

    x_move = 0
    y_move = 0

    cur_x = 0
    cur_y = 0

    direction_speed = 0.5



    cube_dict = {}

    for x in range(20):
        cube_dict[x] = set_vertices(max_distance)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    
                    x_move = direction_speed
                if event.key == pygame.K_RIGHT:
                    
                    x_move = -1*direction_speed
                if event.key == pygame.K_UP:
                    
                    y_move = -1*direction_speed
                if event.key == pygame.K_DOWN:
                    
                    y_move = direction_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0

            #invert the translation

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1)
                if event.button == 5:
                    glTranslatef(0, 0, -1)



        x = glGetDoublev(GL_MODELVIEW_MATRIX)


        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]


        cur_x += x_move
        cur_y += y_move


        glTranslatef(x_move, y_move, .40)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for each_cube in cube_dict:
            cube(cube_dict[each_cube])



        for each_cube in cube_dict:
            if camera_z <=cube_dict[each_cube][0][2]:

                new_Max = int(-1*(camera_z-(max_distance*2)))

                cube_dict[each_cube] = set_vertices(new_Max, int(camera_z-max_distance),cur_x,cur_y)


        pygame.display.flip()
        pygame.time.wait(5)



main()

pygame.quit()
quit()
