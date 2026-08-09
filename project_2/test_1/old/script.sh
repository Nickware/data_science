#!/bin/bash
rm -rf datos
rm -f simulacion
rm -f simulacion.o
nvcc simulation.cu -o simulacion -O3 -std=c++11
mkdir -p datos