# Moth

Note: The Moth project is under active development.

Moth is a new interpreter offering high performance for long-running [Grace](http://gracelang.org/) programs. Moth is built on top of [SOMns v0.6](https://github.com/smarr/SOMns/releases/tag/v0.6.0) and while it achieves great peak-performance we still have some way to go before realizing a complaint Grace implementation.


Contents
--------

To get started have a look at [Getting Ready](#getting-ready) for dependencies and then the [Install](#install) section for information about building the project (or just run `ant` from the root directory of Moth). From there we show how you can invoke tests, benchmarks, and your own programs in [Running Grace](#running-grace).


Status
------

The latest release is reflected by the `master` branch [![Build Status](https://travis-ci.org/richard-roberts/Moth.svg?branch=master)](https://travis-ci.org/richard-roberts/Moth).

Although we are working toward a compliant implementation, Moth doesn't yet implement all of Grace's features. Despite these drawbacks, peak performance is comparable to [V8](https://developers.google.com/v8/) for the AWFY benchmarks; more information can be found in our [preprint](https://arxiv.org/abs/1807.00661).

Getting Ready
-------------

Moth consists of three repositories:

- [SOMns](https://github.com/richard-roberts/SOMns) - our fork that adapts SOMns to provide Grace support,
- [Kernan](http://gracelang.org/applications/grace-versions/kernan/) - a Grace interpreter written in C#, and
- [GraceLibrary](https://github.com/richard-roberts/GraceLibrary) - a collection of Grace programs, tests, and benchmarks designed to be used in Moth.

To successfully build Kernan, you will need to have the [xbuild](http://www.mono-project.com/docs/tools+libraries/tools/xbuild/) installed on your machine. The best way to obtain this is to downloaded the latest release of the [mono](https://www.mono-project.com/download/stable/) (an umbrella project focuses on bringing better cross-platform tooling and support to Microsoft products).

To successfully build SOMns, you will need to have Apache's [ANT](https://ant.apache.org/) command line tool (easily installed through most package managers) and a version of [Java](http://www.oracle.com/technetwork/java/javase/downloads/index.html) that implements the [compiler interface](http://openjdk.java.net/jeps/243). We are currently using version **10.0.1**.

Install
-------

This one is simple, just run our [build script](https://github.com/richard-roberts/Moth/blob/master/build.xml) by invoking `ant` from Moth's root directory. You will first see information about Kernan being built and then SOMns (the Grace library does not need to be compiled). Once everything has been built successfully, you should see something like the following output in your command line:

```sh
Buildfile: .../Moth/build.xml

compile-kernan:
    [echo] Compiling Kernan
    ...
    [exec] Build succeeded.
    [exec]      0 Warning(s)
    [exec]      0 Error(s)
    [exec]
    [exec] Time Elapsed 00:00:06.2428680

compile-somns:
     [echo] Compiling SOMns
     [echo]
     [echo]         ant.java.version: 10
     [echo]         java.version:     10.0.1
     [echo]         is.atLeastJava9:  true
     ...
     compile:
     [echo] Compiling Moth

BUILD SUCCESSFUL
Total time: 2 minutes 7 seconds
```

Provided both Kernan and Moth compiled as expected, you can now run Grace programs using the [moth](https://github.com/richard-roberts/Moth/blob/master/moth) executable:

```sh
./moth GraceLibrary/hello.grace
```

Note that the `moth` executable will first set the `MOTH_HOME` environment variable to Moth's root directory and then start Kernan in the background before running Moth. When Moth is finished, the executable will conclude by terminating Kernan.

Running Grace
-------------

Running a Grace program is simple; you invoke the [moth](https://github.com/richard-roberts/Moth/tree/master/moth) executable from the command line, along with the path to your program as the argument. For example, executing `./moth GraceLibrary/hello.grace` runs the hello world program.

We maintain a small test suite, which can be executed via the [Test Runner](https://github.com/richard-roberts/GraceLibrary/tree/master/Tests/testRunner.grace) using `./moth -tc GraceLibrary/Tests/testRunner.grace` (the `-tc` argument turns on dynamic type-checking, which is required for some of the tests to pass).

Finally, you may also run Moth in benchmarking mode. To do this, execute the [harness](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks/harness.grace) along with a [Grace benchmark](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks) and the iteration numbers you want to use. For example, executing:

```sh
./moth GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/List.grace 100 50
```
