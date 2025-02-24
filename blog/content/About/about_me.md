# About Me

## Nothing special

I am just a broke DIY (do-it-yourself) enthusiast.

After receiving my Mechatronic Engineering degrees: BEng from VNU-HCM (Vietnam) and MSc from SDU (Denmark), I became a software developer for the wind energy sector. Regardless of straight-A grades and a "cum laude" status, I still suck! For real, I graduated without knowing how to wire a stepper motor. This was because high-quality textbooks were too expensive, experimental equipment was limited, zero connections with the local industry, bad teachers, and lazy self. Sounds familiar? I know you, brothers. We all once were students.

Now that I have free time, instead for regrets, I write.

## How I created this blog

As you may have guessed, this blog is fully static. But, with the existence of various static-site generators (Hugo, Jekyll, Gasby), markup languages (Markdown, AsciiDoc, reStructuredText), hosting services (Netlify, AWS Amplify, Vercel), choosing one technology stack is not easy. To avoid the analysis-paralysis trap, let us walk through some important checkpoints:

1. **Target audiences**: future me, other STEM students & industrial practitioners.
2. **Topics**: control theory, dynamical systems, signal processing, machine learning, and implementing them.
3. **Orientation**: Wiki-like knowledge base using Zettelkasten method, neither numbered chapters nor tutorial hell.
4. **Format**: tech blog with code in MATLAB/Simulink/Python and LaTeX-supported notes.
5. **Desired features**: immersive reader, directed graph, fuzzy & full-text search, interactive plots.
6. **Scalability**: might later become a book (> 1Gb), easy to migrate to another tech stack or web host.
7. **Free** as in "free beer"

This list makes our concern clear enough for Google Gemini to come up with a very nice option: convert Jupyter Notebooks to HTML using [Voila](https://github.com/voila-dashboards/voila). Cool. But, Markdown sucks at LaTeX while Voila only offers some ancient themes. Then, until someone does a better job, I will create my own graphic and an AsciiDoc renderer for Jupyter.
