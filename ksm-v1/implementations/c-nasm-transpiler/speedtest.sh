#!/bin/bash
./output ../../examples/ex1.ksm 16
(time (for i in {1..1000}; do (./ksm-output) > /dev/null; done)) 2>&1 | grep s
