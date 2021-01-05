# The Minimum of Michalewicz Function - Evolutionary algorithm optimization

The program finds the minimum of michalewicz function.  </br>
https://www.sfu.ca/~ssurjano/michal.html </br>
</br>
## Usage: </br>
```bash
python optimize.py dimension epochs population_size [parents_share] [verbose] 
```
verbose:</br>
    0 : no trace </br>
    1 : print short </br>
    2 : print all </br>
</br></br>

## Example:
```bash
python optimize.py 2 100 1000 > /res/result_dim_2
```
Command computes minimum of 2-dimension michalewicz function. The comuptation takes 100 epochs and population is 1000 individuals.
