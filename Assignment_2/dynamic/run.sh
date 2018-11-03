#!/usr/bin/env bash
# linking example

CPPFLAGS=`llvm-config --cppflags`
LLVMLIBS=`llvm-config --libs`
LDFLAGS=`llvm-config --ldflags`

clang $CPPFLAGS -O0 -emit-llvm -c module.cpp -o module.bc

# llvm-link $BENCHMARKS/compression/compression.bc module.bc -o gcd2.linked.bc
# llvm-link $BENCHMARKS/gcd/gcd.bc module.bc -o gcd2.linked.bc
# llvm-link $BENCHMARKS/hadamard/hadamard.bc module.bc -o gcd2.linked.bc
llvm-link $BENCHMARKS/welcome/welcome.bc module.bc -o gcd2.linked.bc

llc -filetype=obj gcd2.linked.bc -o=welcome.o

g++ welcome.o $LLVMLIBS $LDFLAGS -o welcome.exe

./welcome.exe
