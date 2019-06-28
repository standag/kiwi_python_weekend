# 3 - Debugging and Testing

## REPL

Interactive shell for Python. Simple run `python` in your shell.

```python
$ python
>>> name = "John"
>>> name.length
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'length'
>>> dir(name)
['__add__', '__class__', ... , '__len__', ... , 'title', 'translate', 'upper', 'zfill']
>>> name.__len__
<method-wrapper '__len__' of str object at 0x7f73420350a0>
>>> # Aaah it's a method
... 
>>> name.__len__()
4
>>> name
'John'
>>> len(name)
4
```

## IPython - ```IP[y]:```

A powerful interactive shell with e.g. syntax highlighting, [TAB]-completion.

```shell 
pip install ipython
```

```python
@localhost ~ $ ipython
IPython 6.0.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: name = "John"
In [2]: name.
         capitalize   encode       format       isalpha      isidentifier
         casefold     endswith     format_map   isascii      islower
         center       expandtabs   index        isdecimal    isnumeric    
         count        find         isalnum      isdigit      isprintable

```
## Debugging - `pdb`, `ipdb`

```shell 
pip install ipdb
```

### Usage in Python <= 3.6

`import pdb; pdb.set_trace()` or `import ipdb; ipdb.set_trace()`

### Usage in Python 3.7+

`breakpoint()`

By default, there is used `pdb` but can be change by environmental variable:

```shell
$ export PYTHONBREAKPOINT=ipdb.set_trace 
```

### Example

```python
def fibbonachi(size):
    x = 0
    y = 1
    for i in range(size):
        y = x + y
        x = y
        breakpoint()
        yield x

print([x for x fibbonachi(10)])
```

## Testing

### pytest package

- Most popular framework
- Many plugins, etc.
- Looks for all `test_*` files and `test_*` functions
- https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run

## Virtual environment

- Python is installed system/user-wide with all the packages
- **Need:** python specific only for your project
**Solution:** virtual environment - via **pipenv**, **virtualenv**, ...

### Setup virtual environment:

```shell
$ mkdir kiwi_python_weekend
$ cd kiwi_python_weekend
$ pip install pipenv
$ pipenv install --python 3.7 
$ pipenv install requests-html
$ pipenv install --dev pylint black==18.9b0 ipdb pytest	
$ pipenv shell 

```

## IDE - everything on one place

Integrated Development Environment (IDE)

Examples:

- VSCode
- PyCharm
- Atom
- ...

**Pros:**

- Intuitive 
- Easy to use

**Cons:**

- You won’t look like a hacker


### Guide for setup Visual Studio Code

https://docs.google.com/document/d/1C0zJGuH9BNdH1gEOZzUBWYRFWKA2-4gXJavv1vLKKxA/edit#heading=h.5gkxopmr4ivt