#!/bin/bash
./build.sh
time (for i in {1..1000}; do (./output ../../examples/ex1.ksm 16) > /dev/null; done)
