# System resolutor using the Echelon method

This piece of code resolve a ```Ax = b``` system, following the echelon method. Cloning this script and setting the A and b matrix/vector, it will return the x vector.
Numpy must be installed to perform the calculations.

## Run the code

To run the code:

```sh
python ./main.py
```

## Code snippet to indicate where to insert your algebraic system
Here it is the test the software execute when it is run:

```python

    A = np.array([[2, 1, -1],
             [-3, -1, 2],
             [-2, 1, 2]])

    b = np.array([8, -11, -3])

    wider_matrix = get_echelon_form(A,b)
    reduced_matrix = reduced_echelon_form(wider_matrix)
    solution = solve_reduce_matrix(reduced_matrix)
    
    ## ------------------  Testing unit  ----------------------------- ##
    
    np.testing.assert_equal(solution, np.array([2 ,3,-1]))
    
    ```

Asserting the system has been solved due to the solution of A and b stated in the code snippet is: [2, 3,-1]
