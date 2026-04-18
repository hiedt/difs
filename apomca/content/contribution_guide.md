# Contribution Guideline

## Toolset

### Document language

APOMCA is a static blog written in [Markedly Structured Text (MyST)](https://myst-parser.readthedocs.io/en/latest/)---a Markdown flavor developed by [the ExecutableBooks team](https://compass.executablebooks.org/en/latest/team/index.html#team). It is then built by [Jupyter Book v1](https://jupyterbook.org/v1/intro.html) and hosted on [Read the Docs (RTD)](https://about.readthedocs.com/). As a result, given the same `.md` file, one should see different rendering on GitHub/Obsidian from my official publication. In fact, MyST is a backward-compatible extension of the original CommonMark. Although you can use the classic style, MyST syntaxes are preferred ([extra configuration may be required](#build-engine)). Here is a [comparison between these two flavors](https://mystmd.org/guide/syntax-overview).

(build-engine)=
### Build engine
Again, it's [Jupyter Book version 1.0 (JB1)](https://jupyterbook.org/v1/intro.html), not the latest version 2.0 found on their homepage. Since JB1 is built on Sphinx, which has no native support for MyST, certain features are turned off by default, most notably `:::{admonition}` for admonitions and `begin{align}` for `amsmath` equations. Follow [this instruction to tell the parser](https://myst-parser.readthedocs.io/en/latest/configuration.html) how to activate them

  1. globally: apply to all source files in a project, settings are stored in `_config.yml`.
  2. locally: apply to an individual file, settings are stored in its front matter.

[Here is the list of all available parameters](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html)

APOMCA has these global features activated

:::{code} yaml
parse:
  myst_enable_extensions:
    - amsmath # LaTeX rendering using MathJax v2.0
    - colon_fence # MyST colon fence for admonitions, code blocks, and figures.
    - dollarmath # LaTeX rendering for $ using MathJax v2.0
    - linkify # Allow bare link
    - substitution # Jinja2 templating
    - tasklist # Checkbox
:::

### Math expressions

Math expressions are written in standard LaTeX and rendered by MathJax v3 which comes by default as a dependency of Sphinx v7.

### Programming language

Julia. I was though using Python when this project started.

## Development Environment Setup
<!-- This section should not be opened to everyone. I will relocate it to GitHub Wiki soon. -->
Make a Python environment using either `pip`, `conda` or `mamba`. I use `mamba` mostly, sometimes `pip` if a package is only available on PyPI.

  ```bash
  mamba create -f dev_env.yaml
  mamba activate difs

  # To rebuild this blog
  jupyter-book build apomca/
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
