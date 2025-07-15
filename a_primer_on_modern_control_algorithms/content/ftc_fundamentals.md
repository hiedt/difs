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

You may have recognized what the operation layer in {numref}`ftc_layers` is—just a conventional block diagram for every control system. In order to tackle a faulty situation, a supervision layer is added by following a four-step framework:

1. Enable redundancy
2. Diagnose faults
3. Employ a recovery mechanism
4. Assess final performance

```{figure} ../assets/ftc_layers.svg
:alt: ftc_layers
:name: ftc_layers

Basic architecture of a fault-tolerant system
```

### Redundancy

> Redundant (adjective)
>
> 3: serving as a duplicate for preventing failure of an entire system (such as a spacecraft) upon failure of a single component.
>
> -- Merriam-Webster dictionary

Replacing a defected device during maintenance is easy but during operation is always infeasible. One strategy in this case is to install (at least) two identical devices and switch between them if one becomes faulty. For example, if a sensor is prone to error, duplicate it; if an actuator is faulty, also duplicate it. This setup, aka. *physical redundancy*, soon becomes very expensive (e.g., debugging time, cost, weight, etc.) for complex machinery.

A better solution is to take advantage of the system's mathematical model, aka. *analytical redundancy*. This extra information allows estimation of the nominal state under faulty conditions, resulting timely diagnosis and correction.

```{important}
Redundancy is a must-have component in every fault-tolerant system. This is obviously true-by-definition.
```

### Diagnosis Module

This module is mostly a software function that utilizes the analytical redundancy, actual control command $u$, and measured output $y$ to do:

- fault detection: when does a fault occur?
- fault isolation: where is it?
- fault estimation: what is its magnitude?

{numref}`ftc_layers` implies an online estimator, i.e., diagnosis is done in real-time using same signals as the main controller during operation. In fact, we only provide online methods across this blog.

```{tip}
Each task has several algorithms that are described in separate pages. You can find them via tags `faultdetection`, `faultisolation`, and `faultestimation`.
```

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
