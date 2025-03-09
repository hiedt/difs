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

1. Make a Python environment using `conda` or `mamba`
2. (optional) As Sphinx is installed by default as a dependency of `jupyter-book`, we only need to install some third-party extensions.
3. Restructure the book folder by modifying `_config.yml` and `_toc.yml`.
4. (optional) Extract Sphinx `config.py` for finer settings. Go to step 5b, then.
5. (a) Build with `jupyter-book` CLI.
(b) Build with `sphinx-build` CLI.

## Suggest Errata

Fork the repo, make some changes, then open a pull request (PR)

## Make Questions

Log an issue on GitHub
