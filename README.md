# Moth

Note: The Moth project is under active development. Some of the information in this document represents my intention rather than the current reality.

Moth is a new interpreter offering high performance for long-running [Grace](http://gracelang.org/) programs. Moth is built on top of [SOMns v0.6](https://github.com/smarr/SOMns/releases/tag/v0.6.0).


Contents
--------

To get started have a look at [Getting Ready](#getting-ready) to see software you will need before getting starting and then see [Install](#install) for information about building the project (just run `ant`).

From there, you might like to check out [Running the Tests](#running-the-tests) or [Running the Benchmarks](#running-the-benchmarks) to see Moth in action, or otherwise check out [Status](#status) for an overview of where we are at with our support for the [Grace programming language](http://gracelang.org/) and [More Details](#more-details) for a bit of information on Moth's design.


Status
------

Although we are working toward a compliant implementation, Moth doesn't yet implement all of Grace's features. In particular, our support for reuse statements (only `inherit` with literal arguments may be used) and type checking is limited to checking only that the given object can respond-to the signatures defined by the type.

Despite these drawbacks, Moth's benchmarks demonstrate impressive peak performance. 

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

This one is simply, just run our [build script](https://github.com/richard-roberts/Moth/blob/master/build.xml) by invoking `ant` from Moth's root directory. You will first see information about Kernan being built and then SOMns (the Grace library does not need to be compiled). Once everything has been built successfully, you should see something like the following output in your command line:

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

More Details
------------

While Moth is responsible for interpreting Grace AST, we use Kernan for parsing the source program (Moth and Kernan communicate over the wire using the Web-Socket protocol, [RFC 6455](https://tools.ietf.org/html/rfc6455)).

More details coming soon.

Running the Tests
-----------------

Moth treats tests as nothing more than a Grace module that implements any number of methods whose signatures begin with "test". 

Tests can be executed via the [Test Runner](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks/harness.grace) by specifying a test module:

```sh
./moth GraceLibrary/Test/testRunner.grace GraceLibrary/Tests/language.grace
```

or, alternatively, executing the runner without arguments will run the built-in tests:

```sh
./moth GraceLibrary/Test/testRunner.grace
```

You can add your own tests to the runner's collection [here](https://github.com/richard-roberts/GraceLibrary/blob/master/Tests/testRunner.grace#L45).

Running the Benchmarks 
---------------------- 
 
Like the tests, Moth treats benchmarks as nothing more than a Grace module. The module must implement a method whose signatures is `benchmark(innerIterations)`.

Benchmarks can be executed via the [harness](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks/harness.grace) by specifying a benchmark module along with three further arguments: the number of outer and inner iterations to perform along with an unused argument. The unused argument is included for compatibility with our benchmarking tool (not included here).

The number of "outer" iterations describes how many times the benchmark should be run overall, while the number of "inner" iterations is passed to the benchmark itself (the benchmarks use this number in different ways).

For example, you can execute the [List](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks/List.grace) benchmark using 100 outer iterations and 50 inner iterations as follows:

```sh
./moth GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/List.grace 100 0 50
```

When invoked, the harness will first load the given module and then repetitively invoke its `benchmark(_)`. The harness records the time spent on each execution of this function; reporting the results to standard out.
