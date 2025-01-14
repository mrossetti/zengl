# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

# [main](https://github.com/szabolcsdombi/zengl/compare/1.2.2...main)

# [1.2.2](https://github.com/szabolcsdombi/zengl/compare/1.2.1...1.2.2)

- Fix broken `Pipeline.vertex_count`, `Pipeline.instance_count` and `Pipeline.first_vertex`

# [1.2.1](https://github.com/szabolcsdombi/zengl/compare/1.2.0...1.2.1)

- Support x86 architecture
- Support raspberry pi

# [1.2.0](https://github.com/szabolcsdombi/zengl/compare/1.1.0...1.2.0)

- Invalid image format error
- Removed `max_varying_components` limit
- Fixed blank screen for osx when double buffering is enabled
- Disabled shadow window configuration for osx
- Simplified examples main loop

# [1.1.0](https://github.com/szabolcsdombi/zengl/compare/1.0.1...1.1.0)

- Implement soft limit for max number of samples
- Implement `Context.limits`
- Validate uniform buffer size
- Blit to screen flushes the command buffer

# [1.0.1](https://github.com/szabolcsdombi/zengl/compare/1.0.0...1.0.1)

- Fix compile issues on multiple platforms
- Build wheels with cibuildwheel

# [1.0.0](https://github.com/szabolcsdombi/zengl/tree/1.0.0)

First stable version
