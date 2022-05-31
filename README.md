## Notes

Unit Testing. No dependecies. A small unit of code like a function.

To install module in tests folder - Tox.

But here simply:

```
# from project root directort ... same level as README.md setup.py
 pip install .
```

To ensure in virtual enviroment:

```
pip list

```

Give access to titlecase module, so that can perform unit tests.

1. Launch pytest from root directory. Call the pytest module. Look in the tests direcotry for pytest.
   python -m pytest tests
2. Extended mode,aka point to source code, aka fake an install.
   From root directory: pip install -e .
3. TOX
