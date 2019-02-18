import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def main():
    pygame.init()
    display = (400, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    # glRotatef(20, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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

        glRotatef(1, 3, 1, 1)
        glColor3fv((0, 1, 0))
        glutWireSphere(1, 100, 20)
        pygame.display.flip()
        pygame.time.wait(10)


main()
