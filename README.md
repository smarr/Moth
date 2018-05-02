# Moth

Note: The Moth project is under active development. Some of the information in this document represents my intention rather than the current reality.

A new Grace interpreter offering high performance for long-running Grace programs. Moth is built on top of [SOMns v0.6](https://github.com/smarr/SOMns/releases/tag/v0.6.0).

See [Getting Started](#getting-started) for more information about building Moth.


Getting Started
---------------

Moth consists of three repositories:

- [SOMns](https://github.com/richard-roberts/SOMns) - our fork that adapts SOMns to provide Grace support,
- [Kernan](http://gracelang.org/applications/grace-versions/kernan/) - a Grace interpreter written in C#, and
- [GraceLibrary](https://github.com/richard-roberts/GraceLibrary) - a collection of Grace programs, tests, and benchmarks designed to be used in Moth.

While SOMns acts as the interpreter of a Grace program, we defer the responsibility of parsing Grace source code to Kernan (SOMns and Kernan communicate over the wire using the Web-Socket protocol, [RFC 6455](https://tools.ietf.org/html/rfc6455)). Consequently, both Kernan and SOMns need to be built before you can run Grace programs.

We provide a [build script](https://github.com/richard-roberts/Moth/blob/master/build.xml), which uses [Apache ANT](https://ant.apache.org/antlibs/dotnet/), to automate the compilation of both projects. ANT can be installed easily with most package managers. With ANT installed, you can compile both projects by running `ant compile` from Moth's root directory.

Once the build script finishes successfully, start Kernan in its web-socket mode via [kernanWS](https://github.com/richard-roberts/Moth/blob/master/kernanWS) and then use the [moth](https://github.com/richard-roberts/Moth/blob/master/moth) executable to run Grace programs:

```sh
./kernanWS &
./moth GraceLibrary/hello.grace
```
