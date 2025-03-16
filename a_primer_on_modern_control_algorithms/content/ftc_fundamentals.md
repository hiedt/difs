# Fundamentals of Fault-tolerant Control (FTC)

In the realm of increasingly complex systems, the imperative for uninterrupted operation grows ever more concerning. This part represents methodologies for building a resilient system which can maintain its stability and performance even when unexpected disruptions like component failures occur. Such resilience is fundamental in safety-critical applications such as aviation, aerospace, medical equipment, etc., where downtime or errors create severe consequences. We can achieve this by following these four steps: enable redundancy, detect error, incorporate a recovery mechanism, then assess the overall integration.

```{Note}
We are **not** concerned about why or how a fault happens. There exists many methods to answer it such as Failure Mode & Effect Analysis (FMEA), which belong to another study field. Here, we will in fact check 'where' they are, then 'how to resolve' them.
```

## Definitions

### Fault vs. Other Factors

*A fault*, in a generic sense, is something that surprisingly changes a system's usual behavior, making it no longer satisfy the desired outcome. Most systems can provide service only when all of their components work as they are designed for. Thus, a fault in one single component may corrupt the whole.

This definition is, though OK to say, not good enough because *a noise*, *a disturbance* and *model uncertainty* also yield same effects. Let's distinguish them by examining a simple {ref}`LTI system <lti>` controlled by a full-state feedback regulator.

$$
\begin{align*}
\dot{x} &= A x + B u \\
u &= -K \hat{x} + N r \\
\hat{x} &= x + e
\end{align*}
$$

```{list-table} Comparison between a fault and other factors
:header-rows: 1
:name: fault_vs_others

* - Fault
  - Noise
  - Disturbance
  - Model uncertainty
* - Rarely happens, often starts to appear after a long time of service due to wear & tear
  - Likely always exists
  - Likely always exists
  - Often exists
* - Can be anywhere
  - Only in sensors (vector $e$)
  - Only in plant (matrices $A, B$)
  - In plant and use case ($A, B, r$)
* - Caused by unknown reasons
  - Caused by environment
  - Caused by environment
  - Bad design by wrong assumptions of maker/user
```

{numref}`fault_vs_others` is just a relative guideline, not a definite truth. In reality, they might be identical, correlated, or causal of each other. For example:

1. When the ambient temperature becomes too cold (disturbance), an airplane's Pitot tube gets frozen (sensor fault).
2. After a long time of heavy operation, intense vibration (model uncertainty) cracks the gear box (actuator fault).
3. A household temperature sensor shows $30^\circ C$ while it is dead-cold indoor. This might either be noise or fault, nobody knows.

In {ref}`detectability`, we will see when it is possible to point out faults from disturbances/noises or not.

### Redundancy

(detectability)=

### Detectability

This metric indicates if we can detect a fault and how reliable our detection is.

```{math}
:label: uio

\begin{align*}
\dot{x} &= A x + B u + E_d d\\
  &= A x + [B ~~ E_d][u~~d]^{\top} \\
  &= A x + B' u' \\
\end{align*}
```

```{hint}
By encapsulating disturbance vector $d$ into input vector $u' = [u~~d]^{\top}$ in equation {eq}`uio`, we can also call a disturbance an *unknown input*.
```
