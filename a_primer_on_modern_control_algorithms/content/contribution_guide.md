# Contribution Guideline

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

## Development Environment Setup
<!-- This section should not be opened to everyone. I will relocate it to GitHub Wiki soon. -->
Make a Python environment using either `pip`, `conda` or `mamba`. I use `mamba` mostly, sometimes `pip` if a package is only available on PyPI.

  ```bash
  mamba create -f dev_env.yaml
  mamba activate difs

  # To rebuild this blog
  jupyter-book build a_primer_on_modern_control_algorithms/
  ```

Jupyter Book is a wrapper of Sphinx, a static-site generator written in Python. The following sub-sections provide tutorial links from which contributors can develop custom themes, build processes, or more advanced features.

### Build a Sphinx Extension

Please follow [this tutorial](https://www.sphinx-doc.org/en/master/development/tutorials/extending_syntax.html#tutorial-extending-syntax).

### Customize Sphinx Theme

Please follow [this tutorial](https://www.sphinx-doc.org/en/master/development/html_themes/index.html).

### Customize Sphinx Build Process

Please follow [this tutorial](https://www.sphinx-doc.org/en/master/extdev/index.html#build-phases).

## Suggest Errata

Fork the repo, make some changes, then open a pull request (PR)

## Make Questions

Log an issue on GitHub
