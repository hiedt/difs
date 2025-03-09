# Welcome to A Primer on Modern Control Algorithms (APOMCA)

In an era functioned by automation and intelligent systems, control theory has become more vital than ever. From precise movements of robotic arms to complex regulation of climate systems, modern control algorithms are the silent architects of our technological world.

APOMCA, written by a graduate student in a pragmatic language, is designed to be your accessible gateway into this fascinating domain. We aim to demystify core concepts, bridging the gap between theoretical foundations and practical applications without overloading mathematics. Whether you are a student, an industrial practitioner, or simply a curious mind, this primer will equip you with the most fundamental knowledge needed to get contemporary control strategies up running.

```{note}
Our blog is fully open-source. It is also under active development so readers are encouraged to examine, leave comments, contribute content, or suggest errata via GitHub issues.
```

## Target Audiences

First and foremost, our future selves. If you are interested in these topics, welcome home fellas.

- Advanced feedback control: optimal/robust/model-reference/predictive control, etc.
- Dynamical systems of many kinds: linear/non-linear, switch, continuous/discrete, etc.
- Analyze those concepts in Python and MATLAB
- Implement binary executables on microcontrollers
- and hopefully more.

## Reader Guide

This blog does not have any numbered chapters. Instead, it is organized as a Wiki-like knowledge base. Readers start by searching a keyword, e.g., "Observability" to open its primary section. From here, you can easily find related pages in the graph view (bottom-right corner).

Each page starts with preliminary knowledge and ends with basic exercises. Answers can be found in [my GitHub repository](https://github.com/hiedt/difs/tree/master/apomca_sol).

## Our Tech Stack

As you may have guessed, this blog is fully static. But, with the existence of various static-site generators (Hugo, Jekyll, Gasby), markup languages (Markdown, AsciiDoc, reStructuredText), hosting services (Netlify, AWS Amplify, Vercel), choosing one technology stack is not easy. To avoid the analysis-paralysis trap, let us walk through some important checkpoints:

1. **Target audiences**: future me, other STEM students & industrial practitioners.
2. **Orientation**: Wiki-like knowledge base (aka. Zettelkasten method)
3. **Format**: tech blog containing MATLAB/Simulink/Python alongside LaTeX notes.
4. **Desired features**: immersive reader, directed graph, fuzzy & full-text search, interactive plots.
5. **Scalability**: might later (hopefully) become a book (> 1Gb), easy to migrate to another tech stack or server host.
6. **Free** as in "free beer"

That list makes our concern clear enough for Google Gemini to suggest this single best choice: write in [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html) using Jupyter Lab, generate static sites using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), then host on [Read the Docs](https://about.readthedocs.com/). Follow [this tutorial](https://medium.com/@soumenatta/publishing-online-books-using-jupyter-book-and-github-pages-5960d809cbb7) if you want to create a tech blog like APOMCA.

A common alternative is either [Voila](https://github.com/voila-dashboards/voila) or [Quarto](https://quarto.org/) being served on GitHub Pages. Although they provide more flexibility with vast customization, I find them quite advanced for newbies. I prefer writing content to debugging tools.

## About Us

More like "About Me" but hopefully, I will find a collaborator soon. My name is [Hieu](https://gravatar.com/hiedt) /hjuː/. I am now writing from Aarhus, Denmark.
