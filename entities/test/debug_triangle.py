from consts.consts import MAIN_ENGINE_PATH
from OpenGL.GL import *

import numpy as np

DEFAULT_VERTEX_PATH = f"{MAIN_ENGINE_PATH}\\entities\\shaders\\default_vertex.vert"
DEFAULT_FRAGMENT_PATH = f"{MAIN_ENGINE_PATH}\\entities\\shaders\\default_fragment.frag"


class DebugTriangle:

    def __init__(self):
        self.vertices = np.array([
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # Bottom-left vertex
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,  # Bottom-right vertex
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0  # Top vertex
        ], dtype=np.float32)

        self.vert_shader_source = self.load_shader_file(DEFAULT_VERTEX_PATH)
        self.frag_shader_source = self.load_shader_file(DEFAULT_FRAGMENT_PATH)

        self.shader_program = self.compile_shaders()
        self.VBO, self.VAO = self.create_buffers()

    def load_shader_file(self, path):
        with open(path, "r") as f:
            source_string = f.read()
        return source_string

    def compile_shaders(self):
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vertex_shader, self.vert_shader_source)
        glCompileShader(vertex_shader)

        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fragment_shader, self.frag_shader_source)
        glCompileShader(fragment_shader)

        shader_program = glCreateProgram()
        glAttachShader(shader_program, vertex_shader)
        glAttachShader(shader_program, fragment_shader)
        glLinkProgram(shader_program)

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        return shader_program

    def create_buffers(self):
        VBO = glGenBuffers(1)
        VAO = glGenVertexArrays(1)

        glBindVertexArray(VAO)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices, GL_STATIC_DRAW)

        # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GL_FLOAT), ctypes.c_void_p(0))
        float32_size = np.dtype(np.float32).itemsize

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * float32_size, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * float32_size, ctypes.c_void_p(3 * float32_size))
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        return VBO, VAO

    def render(self):
        glUseProgram(self.shader_program)
        glBindVertexArray(self.VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glBindVertexArray(0)


if __name__ == "__main__":
    # with open(DEFAULT_VERTEX_PATH, "r") as f, open(DEFAULT_FRAGMENT_PATH, "r") as g:
    #     print(f.read())
    #     print(g.read())

    debug_triangle = DebugTriangle()
    print(debug_triangle.vert_shader_source)
    print(debug_triangle.frag_shader_source)
