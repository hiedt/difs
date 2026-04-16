# What is a dynamical system?

In a nutshell, it is a system whose state changes over time. Mathematicians make this definition more rigorous by using **differential equations**

\begin{align*}
    \dot{x}(t) &= f(x(t)) \\
    x(0) &= \text{a definite value}
\end{align*}

That is:

- the next state $x$ depends on the current state and
- the initial state at t = 0 must be a known and unique constant.

The Fibonacci sequence is a typical example that violates (2) as its initial condition requires two values, i.e., $Fib(0)=1$  and $Fib(1)=1$.

$$
Fib(n) = Fib(n-1) + Fib(n-2)
$$

On the other hand, there exist static systems that are governed by **algebraic equations**

$$
y(t) = f(x(t))
$$

Although it has time as a variable, the current value $y(t)$ does not depend on the past $y(t-1)$. It is just an instant mapping from $x$. In other words, we don't need to wait for $y$ to evolve. That is why nobody controls a static system.

:::{note}
Control engineering only deals with dynamical systems. Our target is to drive them from their starting point $x(0)$ to a desired state $x_{ref}$.
:::
