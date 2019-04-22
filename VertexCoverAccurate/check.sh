#!/bin/bash

timeout=2
graphs=(e5 e10 e20 e40 e150 s25 s50 s500 b20 b30 b100 k330_a k330_b k330_c m20 m30 m40 m50 m100 p20 p35 p60 p150 r30_01 r30_05 r50_001 r50_01 r50_05 r100_005)

find graph -name *.sol -delete

for graph in ${graphs[*]}
do
  echo "Solve graph ${graph}"
  timeout ${timeout} python3 $1 graph/${graph}
done

python3 grademe.py