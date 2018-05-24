# Moth

Note: The Moth project is under active development. Some of the information in this document represents my intention rather than the current reality.

Moth is a new interpreter offering high performance for long-running Grace programs. Moth is built on top of [SOMns v0.6](https://github.com/smarr/SOMns/releases/tag/v0.6.0).

See [Getting Started](#getting-started) for more information about building Moth, and then [Running the Tests](#running-the-tests) and [Running the Benchmarks](#running-the-benchmarks) for more information about running Moth. 


Status
------

Although we are working toward a compliant implementation, Moth doesn't yet implement all of Grace's features. In particular, our support for reuse statements (only `inherit` with literal arguments may be used) and type checking is limited (simply Boyland-style type checks on parameters are supported, but not Grace's full gradual-structural type system).

Despite these drawbacks, Moth's benchmarks demonstrate impressive peak performance. 

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

Support for Boyland-style type checking is turned off by default. Provide the `--boyland-checking` (or `-bc` for short) argument to Moth to enable the checking:

```sh
./moth -bc GraceLibrary/hello.grace
```

Running the Tests
------------------

A Grace test is simply a module that implements any number of methods whose signatures begin with "test". 

The built-in tests can be executed by executing the [Test Runner](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks/harness.grace) without any arguments: `./moth GraceLibrary/Tests/testRunner.grace`. Alternatively, a single test file can be run by providing the path to that test as an argument; for example:

```
./moth GraceLibrary/Test/testRunner.grace GraceLibrary/Tests/basicLanguageFeatures.grace
```

Running the Benchmarks 
---------------------- 
 
*Note: To run the benchmarks and generate the graphs displaying their results, you will need a `Python3` interpreter installed along with the `matplotlib` library.*
 
Benchmarks are nothing more than a Grace module that implements any number of methods whose signatures begin with `benchmark`. For example, the following program is a benchmark:

```
method benchmarkFoo { return "foo" }
method benchmarkBar { return "bar" }
```

You can run a benchmark using `moth` to execute the [harness](https://github.com/richard-roberts/GraceLibrary/tree/master/Benchmarks/harness.grace), along with six arguments:

- `harness`, the path to the Grace harness
- `suite`, the path to the benchmark
- `mode`, the output mode, which can be either `pretty` (for human-readable output) or `csv` (for microsecond execution time output)
- `outer`, the number of times to run each benchmark function for
- `warmup`, the number of warm-ups executions
- `inner`, the number of iterations used during each execution

For example, you can run the Richards benchmark with:

```
./moth GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/richards.grace pretty 100 30 60
```

The harness will first examine the module and find all function whose signature starts with `benchmark`. The harness then runs each of these functions. For each function, the harness first warms up and then executes the benchmark and reports the results. 

The `outer`, `warmup`, and `inner` arguments configures how the harness performs the warm up and execution steps: the `inner` argument defines how many times the benchmark function should be run for one "iteration"; the `warm-up` argument specifies how many of these iterations should be performed before the main execution; and finally, the `outer` describes how many iterations should be reported.

Finally, the mode argument sets the type of output you will get. When using `csv` as the argument, the execution of each outer iteration will be reported in microseconds (good for examining compilation). You can also use `pretty` to get a human-readable report of the average and total run time.

### Automation

To automatically run a Grace benchmark and graph the result, invoke the [benchmark/runSuite](https://github.com/richard-roberts/Moth/tree/master/benchmarks/runSuite) executable with four arguments: the name of the benchmark suite (not its file path), along with the number of outer, warm-up, and inner iterations. For example: 

```sh
./benchmarks/runSuite Richards 100 30 60
```

Alternatively you may also compare the performance across different suits, with the drawback that each suite may only implement one benchmark function. To do this, invoke the [benchmark/runComparison](https://github.com/richard-roberts/Moth/tree/master/benchmarks/runComparison) executable with a comma-separated list of benchmark names.

```sh
./benchmarks/runComparison List,Sieve 100 30 60
```

After the program has finished, you can find both the graph and the raw data in the newly created `output` directory (located inside the moth's root folder).