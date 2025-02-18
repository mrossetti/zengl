# ZenGL

ZenGL is a minimalist Python module providing exactly **one** way to render scenes with OpenGL.

```
pip install zengl
```

- [Documentation](https://zengl.readthedocs.io/)
- [zengl on Github](https://github.com/szabolcsdombi/zengl/)
- [zengl on PyPI](https://pypi.org/project/zengl/)

**ZenGL is ...**

- **high-performance**
- **simple** - *buffers, images, pipelines and there you go*
- **easy-to-learn** - *it is simply OpenGL with no magic added*
- **verbose** - *most common mistakes are catched and reported in a clear and understandable way*
- **robust** - *there is no global state or external trouble-maker affecting the render*
- **backward-compatible** - *it requires OpenGL 3.3 - it is just enough*
- **cached** - *most OpenGL objects are reused between renders*
- **zen** - *there is one way to do it*

## Concept

ZenGL provides a simple way to render from Python. We aim to support headless rendering first,
rendering to a window is done by blitting the final image to the screen. By doing this we have full control of
what we render. The window does not have to be multisample, and it requires no depth buffer at all.

[read more...](https://zengl.readthedocs.io/en/latest/#concept)

## Examples

```
pip install zengl[examples]
```

#### [grass.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/grass.py)

[![grass](https://github.com/szabolcsdombi/zengl/raw/examples/grass.png)](#grasspy)

#### [envmap.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/envmap.py)

[![envmap](https://github.com/szabolcsdombi/zengl/raw/examples/envmap.png)](#envmappy)

#### [instanced_crates.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/instanced_crates.py)

[![instanced_crates](https://github.com/szabolcsdombi/zengl/raw/examples/instanced_crates.png)](#instanced_cratespy)

#### [julia_fractal.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/julia_fractal.py)

[![julia_fractal](https://github.com/szabolcsdombi/zengl/raw/examples/julia_fractal.png)](#julia_fractalpy)

#### [blending.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/blending.py)

[![blending](https://github.com/szabolcsdombi/zengl/raw/examples/blending.png)](#blendingpy)

#### [render_to_texture.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/render_to_texture.py)

[![render_to_texture](https://github.com/szabolcsdombi/zengl/raw/examples/render_to_texture.png)](#render_to_texturepy)

#### [pybullet_box_pile.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/pybullet_box_pile.py)

[![pybullet_box_pile](https://github.com/szabolcsdombi/zengl/raw/examples/pybullet_box_pile.png)](#pybullet_box_pilepy)

#### [pygmsh_shape.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/pygmsh_shape.py)

[![pygmsh_shape](https://github.com/szabolcsdombi/zengl/raw/examples/pygmsh_shape.png)](#pygmsh_shapepy)

#### [texture_array.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/texture_array.py)

[![texture_array](https://github.com/szabolcsdombi/zengl/raw/examples/texture_array.png)](#texture_arraypy)

#### [monkey.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/monkey.py)

[![monkey](https://github.com/szabolcsdombi/zengl/raw/examples/monkey.png)](#monkeypy)

#### [reflection.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/reflection.py)

[![reflection](https://github.com/szabolcsdombi/zengl/raw/examples/reflection.png)](#reflectionpy)

#### [polygon_offset.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/polygon_offset.py)

[![polygon_offset](https://github.com/szabolcsdombi/zengl/raw/examples/polygon_offset.png)](#polygon_offsetpy)

#### [blur.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/blur.py)

[![blur](https://github.com/szabolcsdombi/zengl/raw/examples/blur.png)](#blurpy)

#### [hello_triangle.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/hello_triangle.py)

[![hello_triangle](https://github.com/szabolcsdombi/zengl/raw/examples/hello_triangle.png)](#hello_trianglepy)

#### [hello_triangle_srgb.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/hello_triangle_srgb.py)

[![hello_triangle_srgb](https://github.com/szabolcsdombi/zengl/raw/examples/hello_triangle_srgb.png)](#hello_triangle_srgbpy)

#### [viewports.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/viewports.py)

[![viewports](https://github.com/szabolcsdombi/zengl/raw/examples/viewports.png)](#viewportspy)

#### [points.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/points.py)

[![points](https://github.com/szabolcsdombi/zengl/raw/examples/points.png)](#pointspy)

#### [wireframe_terrain.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/wireframe_terrain.py)

[![wireframe_terrain](https://github.com/szabolcsdombi/zengl/raw/examples/wireframe_terrain.png)](#wireframe_terrainpy)

#### [crate.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/crate.py)

[![crate](https://github.com/szabolcsdombi/zengl/raw/examples/crate.png)](#cratepy)

#### [sdf_example.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/sdf_example.py)

[![sdf_example](https://github.com/szabolcsdombi/zengl/raw/examples/sdf_example.png)](#sdf_examplepy)

#### [sdf_tree.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/sdf_tree.py)

[![sdf_tree](https://github.com/szabolcsdombi/zengl/raw/examples/sdf_tree.png)](#sdf_treepy)

#### [mipmaps.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/mipmaps.py)

[![mipmaps](https://github.com/szabolcsdombi/zengl/raw/examples/mipmaps.png)](#mipmapspy)

#### [conways_game_of_life.py](https://github.com/szabolcsdombi/zengl/blob/main/examples/conways_game_of_life.py)

[![conways_game_of_life](https://github.com/szabolcsdombi/zengl/raw/examples/conways_game_of_life.png)](#conways_game_of_lifepy)

#### Headless

```py
import zengl
from PIL import Image

ctx = zengl.context(zengl.loader(headless=True))

size = (1280, 720)
image = ctx.image(size, 'rgba8unorm', samples=1)

triangle = ctx.pipeline(
    vertex_shader='''
        #version 330

        out vec3 v_color;

        vec2 positions[3] = vec2[](
            vec2(0.0, 0.8),
            vec2(-0.6, -0.8),
            vec2(0.6, -0.8)
        );

        vec3 colors[3] = vec3[](
            vec3(1.0, 0.0, 0.0),
            vec3(0.0, 1.0, 0.0),
            vec3(0.0, 0.0, 1.0)
        );

        void main() {
            gl_Position = vec4(positions[gl_VertexID], 0.0, 1.0);
            v_color = colors[gl_VertexID];
        }
    ''',
    fragment_shader='''
        #version 330

        in vec3 v_color;

        layout (location = 0) out vec4 out_color;

        void main() {
            out_color = vec4(v_color, 1.0);
        }
    ''',
    framebuffer=[image],
    topology='triangles',
    vertex_count=3,
)

image.clear_value = (1.0, 1.0, 1.0, 1.0)
image.clear()
triangle.render()

Image.frombuffer('RGBA', size, image.read(), 'raw', 'RGBA', 0, -1).save('hello.png')
```
