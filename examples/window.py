import sys
from OpenGL import GL, GLUT

def init():
    GLUT.glutInit(sys.argv)
    GLUT.glutInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
    GLUT.glutInitWindowSize(800, 600)
    GLUT.glutInitWindowPosition(100, 100)
    GLUT.glutCreateWindow("Something!")
    GL.glClearColor(0, 0, 0, 0)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, [0.0, 3.0, 3.0, 0.0])
    GL.glLightModelfv(GL.GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    GL.glEnable(GL.GL_LIGHTING)
    GL.glEnable(GL.GL_LIGHT0)
    GLUT.glutDisplayFunc(update)
    GLUT.glutMainLoop()

def update():
    print 'update'
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, [0.1745, 0.0, 0.1, 0.0])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, [0.1, 0.0, 0.6, 0.0])
    GL.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, [0.7, 0.6, 0.8, 0.0])
    GL.glMaterialf(GL.GL_FRONT, GL.GL_SHININESS, 80)
    GLUT.glutSolidTeapot(0.5)
    GL.glFlush()

if __name__ == '__main__':
    init()

