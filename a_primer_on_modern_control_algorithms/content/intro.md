# Welcome to APOMCA

In an era functioned by automation and intelligent systems, control theory has become more vital than ever. From precise movements of robotic arms to complex regulation of climate systems, modern control algorithms are the silent architects of our technological world.

APOMCA, written by a graduate student in a pragmatic language, is designed to be your accessible gateway into this fascinating domain. We aim to demystify core concepts, bridging the gap between theoretical foundations and practical applications without overloading mathematics. Whether you are a student, an industrial practitioner, or simply a curious mind, this primer will equip you with the most fundamental knowledge needed to get contemporary control strategies up running.

```{note}
Our blog is fully open-source. It is also under active development, so readers are encouraged to examine, leave comments, contribute content, or suggest errata via GitHub issues.
```

## Target Audiences

First and foremost, our future selves when we need to resharpen our skills on the following topics. If you share the same interest, then welcome home fellas.

- Cutting-edge feedback loops:
  - Optimal control like LQR or MPC
  - Adaptive control like MRAC
  - Robust control like sliding mode
  - Data-driven like reinforcement learning
- Dynamical system analysis
- Apply those concepts in Python and MATLAB
- Execute them on microcontrollers

## To Use This Blog Effectively

This blog does not have any numbered chapters. Instead, it is organized as a Wiki-like knowledge base. Readers start by searching a keyword, e.g., "observability" to open a relevant page, then expand to related topics using the graph view in the bottom-right corner.

Each page starts with a list of preliminary knowledge and ends with basic exercises. Answers can be found in [my GitHub](https://github.com/hiedt/difs/tree/master/apomca_sol). We encourage you to {ref}`make a learning environment <rep_guide>`, peruse our lectures & reproduce the results, then write your own solutions before watching ours.

(rep_guide)=

## Try Solving the Exercises by Yourself

1. Open a terminal (e.g., Windows Command Prompt or Powershell), install Python & one package mananger such as `pip`, `conda`, or `mamba`. For simplicity, I will use `pip` here.
2. Clone & open this repository

  ```bash
  git clone https://github.com/hiedt/difs
  ```

3. Installed required packages

  ```bash
  pip install -r a_primer_on_modern_control_algorithms/requirements.txt
  ```

4. *(Optional)* Open a notebook editor, i.e., Jupyter Lab, and start coding

  ```bash
  jupyter lab
  ```

Happy learning. 🥳

```{include} contribution_guide.md
```

```{include} about_us.md
```
