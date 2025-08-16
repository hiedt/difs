# Welcome to APOMCA

*A Primer On Modern Control Algorithms* is written by a graduate student, hence the pragmatic language that provides easy access to the fascinating domain of control engineering. Whether you are a student, an industrial practitioner, or simply a curious mind with a relevant background, this primer will help you quickly understand core concepts before tutoring your own implementation.

```{tip}
My blog is fully open-source and under active development. Readers are encouraged to examine, leave comments, contribute content, or suggest errata via GitHub issues.
```

## Target Audiences

First and foremost, my future self when I need to sharpen my memory about the following topics:

- Software for embedded applications
- Fault-tolerant control
- Theory of (linear & non-linear) dynamical systems
- Statistical signal processing
- Optimal control, with a quick glance through reinforcement learning
- Robust control

I use mostly materials from my Master's degree in Mechatronics at the University of Southern Denmark back in 2024. Thus, readers should be familiar with basic terms such as:

- Linear time-invariant systems (LTI), tranfer functions, state space
- Frequency response, Bode plot, Nyquist plot
- PID, integral windup, pole placement, gain scheduling
- Linear algebra, probability & statistics, numerical methods (No worries! These math tools will be reviewed in appendices as I don't remember them, either.)

I will do my best to provide enough foundation without copy-pasting too much rigorous math proofs from textbooks.

## To Use This Blog Effectively

This blog does not have any numbered chapters. Instead, it is organized as a Wiki-like knowledge base. Readers start by searching a keyword, e.g., "observability" to open a relevant page, then expand to related content via reference links.

Each page starts with a list of preliminary knowledge and ends with basic exercises. Answers can be found in [this repo](https://github.com/hiedt/difs/tree/master/apomca_sol). I encourage you to first peruse the lectures, reproduce the results, then do your own work before watching my solutions.

<!--TODO: ## To Work by Yourself -->
<!--TODO: instruction how to run the page on BinderHub -->

## Technology Stack

The blog is written in MyST Markdown (text) and Julia (code) using [Jupyter Book v1](https://jupyterbook.org/en/stable/intro.html) ([default theme](https://sphinx-book-theme.readthedocs.io/en/stable/sections/sidebar-primary.html)), which is then built and hosted by [ReadtheDocs.io](https://about.readthedocs.com/?ref=app.readthedocs.org). I use VSCode's [extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) for most modification, whereas pilot testing is done on [Binder](https://mybinder.org/).

"Why Julia?"---you ask. Julia is well-designed for scientific computing. It has superb performance, GPU support, one-indexed, first-class arrays, data plotting, etc. natively. Python, on the other hand, is more general-purpose, so you need to install multiple packages like Numpy, SciPy, or Matplotlib. MATLAB...😶!

## References

Here are the textbooks I use.
