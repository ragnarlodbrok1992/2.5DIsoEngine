import glfw

from OpenGL.GL import *


TITLE_BAR = "IsoEngine"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 768


def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        # Set window should close flag to True
        glfw.set_window_should_close(window, True)


def main():
    # Intialize glfw
    if not glfw.init():
        return

    # Set OpenGL version to 3.3 and use core profile
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE_BAR, None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set key callback
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Render here
        glClear(GL_COLOR_BUFFER_BIT)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    # Terminate glfw
    glfw.terminate()


if __name__ == "__main__":
    main()
