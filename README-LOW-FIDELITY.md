# Introduction:

This document uses markdown and is best read in a markdown-capable viewer such as github.

# Notes
* The prototype/ directory contains rough, first-draft code aimed at proving that:
* The unittests/ directory contains basic unit testing of algorithmic concepts
* Test an algorithm that navigates given a set of instructions
* Test an algorithm calculating distance and tracking coordinates works
* Test an algorithm detecting loops returning to origin works
 
# Tests
Three unit tests were provided, proving the core of the algorithms

# Design
This prototype does not have any design, as that will emerge during the BDD process. This prototype is all about 
de-risking and exploring the solution space rapidly and in a targeted manner.
 
# Running
## Test suite
```
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python unittests/tests.py

...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

```

## Implementation
```
$ source venv/bin/activate
$ pip install -r requirements.txt

$ python prototype/main.py features/data/valid.instructions
2.236 unit
False

$ python prototype/main.py features/data/movementincludinglargecircle.instructions
3.000 units
True
```

