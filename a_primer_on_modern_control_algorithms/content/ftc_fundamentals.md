# Fundamental Concepts of Fault-tolerant Control

In a modern realm of increasingly complex systems, the imperative for uninterrupted operation grows ever more concerning. This part represents methodologies for building a robust system which can maintain its stability and performance even when unexpected faults occur. Such resilience is a cornerstone of safety-critical applications in aviation, aerospace, medical equipment, wind turbines, etc., where one small defect can create severe consequences.

```{Note}
We do **not** concern about why/how a fault happens nor its propagation effects. There exist many tools belonging to the System Engineering field to answer those questions. Here, we only focus on finding where they are and how to resolve them.
```

## What is a fault?

Generally speaking, *a fault* is something wrong that surprisingly changes a system's usual behavior, hence unsatisfactory outcome. It can happen at the sensor, actuator, or plant, e.g., slower flow through a pipe due to clogging calcium stains from hard water. ({numref}`plant_fault`).

``````{list-table}
:header-rows: 1
:name: common_faults

* - Plant fault
  - Sensor fault
* - ```{figure} ../assets/hardwater.png
    :name: plant_fault

    Clogged pipe
    ```
  - ```{figure} ../assets/frozen_pitot.png
    :name: sensor_fault

    Frozen pitot tube
    ```
``````

### Fault vs. Error

Despite some linguistic nuances, let us use *fault* and *component error* synonymously in this blog. Please, do not mistake *component error* with *measurement error* $e = \hat{x} - x$.

### Fault vs. Failure vs. Danger

Most systems can only work when all components collaborate smooothly as they are designed for ({numref}`op_regions`, green zone). This is also the region in which a system should remain throughout most of its lifetime. When a fault appears, its performance degrades, but still within an acceptable level (orange zone). If this fault is not addressed timely, the system may become entirely dysfunctional aka. *failure* (red zone). Any degradation beyond this red line causes damage to machine, environment, and human aka. *danger* (white zone).

```{figure} ../assets/op_region.svg
:alt: op_regions
:name: op_regions

Performance space of a (faulty) system
```

### Fault Tolerance vs. Safety

Fault tolerance is an ability to work fine under faults. In other words, a fault-tolerant controller must be able to:

- cover a fault (component level) by bringing an orange state back to green, or at least remain there.
- prevent a fault from causing a failure (system level).
- prevent a failure from causing a danger (eco-system level).

Safety refers to the absence of danger. If the controller cannot maintain a safe status, i.e., system performance crosses the red line, another entity called *a safety system*:

- is implemented as a separate part, hardware and software-wise.
- shuts down a failing machine's operation, or at least keeps it within the safe zone.

As they are complementary and equally important, you can usually find both in most industrial settings. This partition allows fault-tolerant control development to be free from most safety standard compliance.

```{tip}
Safety and safety system are not discussed further in this blog.
```

### Fault vs. Other Factors

Besides faults, *a noise*, *a disturbance* and *model uncertainty* also yield similar effects. Let's distinguish them by examining a simple {ref}`LTI system <lti>` controlled by a full-state feedback regulator.

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
* - Caused by any reason, even by noise and disturbance
  - Caused by environment
  - Caused by environment
  - Poor design by engineers
* - Controller **should workaround** fault
  - Noise must be handled **by filters, not controllers**
  - Controller **must eliminate** disturbance
  - Engineers **must consider** model uncertainty during controller design
```

{numref}`fault_vs_others` is just a relative guideline, not a definite truth. In fact, they might be identical, correlated, or causal of each other. For example:

1. When the ambient temperature becomes too cold (disturbance), an airplane's Pitot tube gets frozen (sensor fault, {numref}`sensor_fault`), causing the befamous crash of [Air France AF447](https://en.wikipedia.org/wiki/Air_France_Flight_447) (failure).
2. After a long time of heavy operation, intense vibration (model uncertainty) cracks the gear box (actuator fault).
3. A household temperature sensor shows $30^\circ C$ while it is dead-cold indoor. This might either be noise or fault, nobody knows.

In {ref}`detectability`, we will see when it is possible to distinguish faults from noise/disturbance.

## Components of a Fault-tolerant System

### Redundancy

Redundancy refers to.

### Decision Maker (Agent)

### Recovery Mechanism

## Characteristics of a Fault-tolerant System

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

```{tip}
By encapsulating disturbance vector $d$ into input vector $u' = [u~~d]^{\top}$ in equation {eq}`uio`, we can also call a disturbance an *unknown input*.
```

### Reliability
