# Welcome to APOMCA

```{attention} DISCLAIMER
The code found in this blog is intended for pedagogical purposes, DO NOT use them in production. My blog is under active development, so readers are encouraged to examine, leave comments, contribute content, or suggest errata via GitHub issues.
```

All machines around our daily lives, from cars to dryers, need to be controlled. Thus, understanding control engineering is essential for building systems that are stable, efficient, and safe. *A Primer On Modern Control Algorithms* provides everyone easy access to this fascinating field. Here, *modern* refers to the latest evolution stage (1960s until now) since which people have expanded their scope from frequency-domain and single-input-single-output (SISO) to time-domain and multi-input-multi-output (MIMO).

## Target Audiences

First and foremost, my future self. Then to the students and industry practitioners. Materials are borrowed from my Master's degree in Mechatronics at the University of Southern Denmark back in 2022-2024. Instead of copying rigorous mathematic proofs from textbooks, I choose a pragmatic "given-when-then-example" style so that anyone can quickly grasp the idea how an algorithm works and when to use it.

## Blog Structure

This blog does not have any numbered chapters. Instead, it is a Wiki of pages and links between them. Each page is tagged with keywords. Pages sharing the same topic are grouped into a section, for example,

- Dynamical System Modeling
  - System character: stability, frequency response, linearity, controllability, observability, etc.
  - Math model: transfer function, state space, ordinary differential equations (ODE)
- Statistical Signal Process
  - Signal character: analog, digital, conversion between analog & digital, frequency, amplitude, noise, etc.
  - Processing tool: filter, linearization, anti-aliasing, etc.
- Fault-tolerant Control
  - System characters in erroneous conditions
  - Fault diagnosis & recovery
  - Safety standard and failure mode analysis
- Optimal Control
  - Best strategy that balances between cost & performance
  - Constraints
  - Reinforcement learning as a controller
- *and more*

Each page starts with a list of preliminary knowledge and ends with some basic exercises whose [answers can be found here](https://github.com/hiedt/difs/tree/master/apomca_sol).

## Reader Guide

To use this blog effectively, readers are advised against sequentially jumping through page by page. It is better to start by searching a keyword, e.g., "observability", for the most relevant entry point, then continue expanding to other topics via reference links. Tags is also an effective way to query. Newbies with zero experience can get started with the easiest application: [balance an inverted pendulum using PID](#pid).

<!--TODO: ## To Work by Yourself -->
<!--TODO: instruction how to run the page on BinderHub -->
