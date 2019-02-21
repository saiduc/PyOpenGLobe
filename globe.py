import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def main():
    pygame.init()
    display = (400, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.key.set_repeat(1, 10)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    lastPosX = 0
    lastPosY = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Rotation with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(1, 0, -1, 0)
                if event.key == pygame.K_UP:
                    glRotatef(1, -1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(1, 1, 0, 0)

            # Zoom in and out with mouse wheel
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # wheel rolled up
                    glScaled(1.05, 1.05, 1.05)
                if event.button == 5:  # wheel rolled down
                    glScaled(0.95, 0.95, 0.95)

            # Rotate with mouse click and drag
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                dx = x - lastPosX
                dy = y - lastPosY
                mouseState = pygame.mouse.get_pressed()
                if mouseState[0]:

                    modelView = (GLfloat * 16)()
                    mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)

                    # To combine x-axis and y-axis rotation
                    temp = (GLfloat * 3)()
                    temp[0] = modelView[0]*dy + modelView[1]*dx
                    temp[1] = modelView[4]*dy + modelView[5]*dx
                    temp[2] = modelView[8]*dy + modelView[9]*dx
                    norm_xy = math.sqrt(temp[0]*temp[0] + temp[1]
                                        * temp[1] + temp[2]*temp[2])
                    glRotatef(math.sqrt(dx*dx+dy*dy),
                              temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)

                lastPosX = x
                lastPosY = y

            # rotate(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Adds Lighting, not using for now
        # glShadeModel(GL_SMOOTH)
        # glEnable(GL_CULL_FACE)
        # glEnable(GL_DEPTH_TEST)
        # glEnable(GL_LIGHTING)
        # lightZeroPosition = [45., 4., 10., 1.]
        # lightZeroColor = [0.8, 1.0, 0.8, 100.0]  # green tinged
        # glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        # glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        # glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        # glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        # glEnable(GL_LIGHT0)
        # glRotatef(1, 1, 1, 1)
        glColor3fv((0, 1, 0))
        glutWireSphere(1, 100, 20)
        # glutSolidSphere(1,100,20)
        pygame.display.flip()
        pygame.time.wait(10)


main()
