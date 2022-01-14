#!/bin/bash
time (for i in {1..1000}; do (./output ../../examples/ex1.ksm 4) > /dev/null; done)
