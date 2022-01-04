#!/bin/bash
time (for i in {1..1000}; do (python3 src/main.py ../../examples/ex1.ksm) > /dev/null; done)
