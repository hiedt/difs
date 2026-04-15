# Fault Detection using Parity Method

The following code examples show how MyST Markdown renders tabbed code blocks by using Jupyter Book.

````{tab-set}
```{tab-item} Python
```python
import numpy as np

x = np.array([[1], [2], [3]]) # A 3x1 state vector

A = np.random.rand(3,3) # A 3x3 dynamical matrix

dx = np.dot(A,x)
```

```{tab-item} MATLAB
```matlab
x = rand(3,1);
A = rand(3,3);
dx = A*x
````
