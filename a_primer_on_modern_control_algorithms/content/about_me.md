# About Me

## DIFS means "do it from scratch"

That being said, I am just a broke tech-maker. Nevertheless, I am a father of one cat and I knit our own clothes.

After receiving my Mechatronic Engineering degrees: BEng from VNU-HCM (Vietnam), later MSc from SDU (Denmark), I became a software developer for the wind energy sector. Regardless of a straight-A, also a "cum laude" status, I still suck! Seriously, I graduated without knowing how to wire a stepper motor. This was because high-quality textbooks were too expensive, experimental equipment was limited, zero connections with the local industry, bad teachers, competitive peers, and lazy self. Sounds familiar? I know you, brothers. We all once were students.

Now that I have free time, instead of regretting, I write.

## How I build this blog

As you may have guessed, this blog is fully static. But, with the existence of various static-site generators (Hugo, Jekyll, Gasby), markup languages (Markdown, AsciiDoc, reStructuredText), hosting services (Netlify, AWS Amplify, Vercel), choosing one technology stack is not easy. To avoid the analysis-paralysis trap, let us walk through some important checkpoints:

1. **Target audiences**: future me, other STEM students & industrial practitioners.
2. **Topics**: control theory, {hoverxref}`dynamical systems<dynasys_properties>`, signal processing, machine learning, and how to implement them.
3. **Orientation**: Wiki-like knowledge base (aka. Zettelkasten method), neither numbered chapters nor tutorial hell.
4. **Format**: tech blog containing MATLAB/Simulink/Python alongside LaTeX notes.
5. **Desired features**: immersive reader, directed graph, fuzzy & full-text search, interactive plots.
6. **Scalability**: might later (hopefully) become a book (> 1Gb), easy to migrate to another tech stack or web host.
7. **Free** as in "free beer"

That list makes our concern clear enough for Google Gemini to suggest this single best choice: write in [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html) using Jupyter Lab, generate static sites using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), then host on [Read the Docs](https://about.readthedocs.com/). Follow [this tutorial](https://medium.com/@soumenatta/publishing-online-books-using-jupyter-book-and-github-pages-5960d809cbb7) if you want to create a tech blog like mine.

A common alternative is either [Voila](https://github.com/voila-dashboards/voila) or [Quarto](https://quarto.org/) being served on GitHub Pages. Although they provide more flexibility with vast customization, I find them quite advanced for newbies. I prefer writing content to debugging tools.

## Step-by-step Guide

<!-- TODO: *update section* -->

1. Make a Python environment using `conda` or `mamba`
2. (optional) As Sphinx is installed by default as a dependency of `jupyter-book`, we only need to install some third-party extensions.
3. Restructure the book folder by modifying `_config.yml` and `_toc.yml`.
4. (optional) Extract Sphinx `config.py` for finer settings. Go to step 5b, then.
5. (a) Build with `jupyter-book` CLI.
(b) Build with `sphinx-build` CLI.
