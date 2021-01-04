#!/bin/sh

cd ~/studia/zum/GA/py;

# Dim 2, 100 epochs, 1000 population
python optimize.py 2 100 1000 > /res/result_dim_2;

# Dim 5, 100 epochs, 1000 population
python optimize.py 5 100 1000 > /res/result_dim_5;

# Dim 10, 200 epochs, 10000 population
python optimize.py 10 200 10000 > /res/result_dim_10;


# Verbose

# Dim 2, 100 epochs, 1000 population
python optimize.py 2 100 1000 0.5 2 > /res/result_dim_2_verbose;

# Dim 5, 100 epochs, 1000 population
python optimize.py 5 100 1000 0.5 2 > /res/result_dim_5_verbose;

# Dim 10, 200 epochs, 10000 population
python optimize.py 10 200 10000 0.5 2 > /res/result_dim_10_verbose;