from consts.consts import MAIN_ENGINE_PATH

DEFAULT_VERTEX_PATH = f"{MAIN_ENGINE_PATH}\\entities\\shaders\\default_vertex.vert"
DEFAULT_FRAGMENT_PATH = f"{MAIN_ENGINE_PATH}\\entities\\shaders\\default_fragment.frag"


class DebugTriangle:

    def __init__(self):
        self.vert_shader = None
        self.frag_shader = None


if __name__ == "__main__":
    with open(DEFAULT_VERTEX_PATH, "r") as f, open(DEFAULT_FRAGMENT_PATH, "r") as g:
        print(f.read())
        print(g.read())
