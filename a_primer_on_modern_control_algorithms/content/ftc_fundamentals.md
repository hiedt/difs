# Fundamentals of Fault-tolerant Control (FTC)

In the realm of increasingly complex systems, the imperative for uninterrupted operation grows ever more concerning. This part represents methodologies for building a resilient system which can maintain its stability and performance even when unexpected disruptions like component errors occur. Such resilience is fundamental in safety-critical applications such as aviation, aerospace, medical equipment, etc., where downtime or failures create severe consequences. We can achieve this by following these four steps:

1. Enable redundancy
2. Diagnose the problem
3. Construct a recovery mechanism
4. Finally, assess the overall integration

```{Note}
We are **not** concerned about why or how a fault happens. There exists many methods which belong to another study field to answer those questions. Here, we focus on where they are as well as how to resolve them.
```

## Fault vs. Failure

Generally speaking, *a fault* is something that surprisingly changes a system's usual behavior, making it no longer satisfy the desired outcome. It can happen at the sensor, actuator, or plant, e.g., slower flow through a pipe due to clogging calcium stains from hard water. ({numref}`actuator_fault`).

In reality, most systems can provide service only when all of their components collaborate as they are designed for. Thus, when a fault comes, our controller must be able to workaround it, so that they--as a whole remains operational. Otherwise, the system would be shut down completely. This inability to recover to a functional state is *a failure*.

```{tip}
Fault-tolerant control has to prevent a fault (component level) from causing a failure (system level).
```

``````{list-table}
:header-rows: 1
:name: common_faults

* - Actuator fault
  - Sensor fault
* - ```{figure} ../assets/hardwater.png
    :name: actuator_fault

    Clogged pipe
    ```
  - ```{figure} ../assets/frozen_pitot.png
    :name: sensor_fault

    Frozen pitot tube
    ```
``````

## Fault vs. Other Factors

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

1. When the ambient temperature becomes too cold (disturbance), an airplane's Pitot tube gets frozen (sensor fault, {numref}`sensor_fault`), causing the befamous crash of [Air France AF447](https://en.wikipedia.org/wiki/Air_France_Flight_447) (failure).
2. After a long time of heavy operation, intense vibration (model uncertainty) cracks the gear box (actuator fault).
3. A household temperature sensor shows $30^\circ C$ while it is dead-cold indoor. This might either be noise or fault, nobody knows.

In {ref}`detectability`, we will see when it is possible to point out faults from disturbances/noises or not.

(detectability)=

## Detectability

This metric indicates if we can detect a fault and how reliable our detection is.

```{math}
:label: uio

\begin{align*}
\dot{x} &= A x + B u + E_d d\\
  &= A x + [B ~~ E_d][u~~d]^{\top} \\
  &= A x + B' u' \\
\end{align*}
```

```{tip}
By encapsulating disturbance vector $d$ into input vector $u' = [u~~d]^{\top}$ in equation {eq}`uio`, we can also call a disturbance an *unknown input*.
```

## Redundancy

Redundancy refers to.

### Physical Redundancy

Why is there no indentation for 3rd level headings?

### Analytical Redundancy
Why is there no indentation for 3rd level headings?
