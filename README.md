# Setup Instructions

## Links

- [Python Knowledgebase](knowledgebase/README.md)


## `pyenv`

[`pyenv`](https://github.com/pyenv/pyenv) is a Python version manager (like
`rbenv` for Ruby and `SDKMan!` for Java).  It allows us to set up multiple
Python versions without interfering with system installations.  Different
projects can use different Python versions, and a `.python-version` file can be
added to the project's root directory to control the version automatically.

First install `pyenv` using Homebrew:

```bash
brew install pyenv
```

Add the following commands to `~/.bash_profile` to set up `pyenv` in new shells:

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Then use `pyenv` to install the required version of Python.  Here we're using
version 3.11.7:

```bash
# Use whatever version you want - here we're using 3.11.7
pyenv install 3.11.7
```

To configure a working copy to use this version, either run `pyenv local 3.11.7`
in the working directory, or add a `.python-version` file containing `3.11.7` to
the project root.


## Environment Creation and Dependencies with `venv`:

Run the following commands to set up the virtual environment and install
dependencies for the project:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```


## Testing Matplotlib in IPython

To test Matplotlib in IPython, open a new IPython shell and run:

```
%matplotlib
```

If everything is working, you should get the following response:

```
Using matplotlib backend: MacOSX
```

Then run the following commands:

```python
import numpy as np
import matplotlib.pyplot as plt
plt.plot(np.random.randn(50))
```

A plot window should appear with a plot of random numbers.
