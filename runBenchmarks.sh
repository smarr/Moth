#!/bin/bash

# AWFY Micro
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Bounce.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Fannkuch.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/List.grace 1 10 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Mandelbrot.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/NBody.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Permute.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Queens.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Sieve.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Storage.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Towers.grace 1 1 &&

# AWFY Macro
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/CD.grace 1 10 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/DeltaBlue.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Havlak.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Json.grace 1 1 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Richards.grace 1 1 &&

# Other
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/GraphSearch.grace 1 20 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/SpectralNorm.grace 1 10 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Float.grace 1 10 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Go.grace 1 10 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/PyStone.grace 1 10 &&
./moth -tc -eft GraceLibrary/Benchmarks/harness.grace GraceLibrary/Benchmarks/Snake.grace 1 1 &&

echo "Finished Benchmarks"