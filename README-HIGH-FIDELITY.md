# Introduction:

This document uses markdown and is best read in a markdown-capable viewer such as github.

You can run the program in this repository and it will output the distance and whether the loop return value was True or
False.

# Notes
* This code was developed using a behaviour driven approach using behave as BDD framework.
* Each feature was implemented in a TDD manner, writing the test first, writing the code to make the test pass,
  then refactoring the design.
* The code was produced using PyCharm community edition 2020.1 using a virtualenv environment, running python 3.7.7
* The code features type hinting.
* The robot outputs to the file robot.log using standard python logging. The log is cleared when-ever operate() is called
* The robot can also be asked to verbosely log debug entries by passing the optional debug=True to operate()
* This robot resets its position to (0,0) and its direction to 'n' every time operate() is called
* This implementation is verbose and attempts to be human friendly when dealing with direction. It is also possible
  to implement direction as an integer that wraps around in either direction when turning.
* I love clean code and strive to keep functions to 4-6 lines. For high fidelity implementations it is important though
to include validation and strategic debug code as well.

# Design
The Robot class consist of an interpreter and a navigator. The interpreter reads the instructions and asks the navigator
to perform the necessary actions. The robot then asks its navigator what the distance traveled is and whether circles
were completed. A future design improvement would be to change the Containment relationshiop for the Robot re: the
Interpreter and Navigator to be one of Aggregation and inject these into the Robot on start-up.

# Non-functional requirements
* When reading the instruction file, it can either be parsed line by line and instructions executed as parsed, or all
  lines at once and there-after instructions executed. In this implementation I opted to read all instructions at once,
  then iterate, skipping invalid ones and empty lines and executing valid instructions. I.e. this
  implementation favours the NFR 'compensate for instruction media failure'. If this was executing on mars rover for
  example, one might determine the likelihood of RAM corruption or failure to be higher and since there also would be
  limited RAM to work with, one might favour an alternative approach. Another NFR might be to parse all instructions
  and reject the entire instruction set if some instructions are invalid. In that case, this implementation would
  already have the full list of instructions available for validation and could easily be adapted to reject if invalid.

# Running
## Test suite
```
$ source venv/bin/activate
$ pip install -r requirements.txt
$ behave

3 features passed, 0 failed, 0 skipped
19 scenarios passed, 0 failed, 0 skipped
98 steps passed, 0 failed, 0 skipped, 0 undefined

```

## Implementation
```
$ source venv/bin/activate
$ pip install -r requirements.txt

$ python main.py features/data/valid.instructions
$ cat robot.log

2.236 unit
False

$ python main.py features/data/movementincludinglargecircle.instructions
$ cat robot.log
Warning: some instructions were invalid

3.000 units
True
```

# Assumptions:
* A circle is identified as follows:
    'Any path that returns the robot to the origin (i.e. a loop of some kind) even if the robot crosses its own path
    one or multiple times?'
  The robot is required to make at least one move in order for a circle to be detected. Staying at the origin and
  just turning does not constitute a 'return to the origin'. This behaviour can be easily changed though.


# APIs
## Robot
* robot.nav -> Navigator
* robot.debug -> bool
* robot.operate(instructions_file: str, debug: bool = False) -> bool
* robot.get_notifications() -> [str]

## Navigator:
* navigator.direction -> str
* navigator.distance -> int
* navigator.loops -> int
* navigator.report() -> int
* navigator.reset()
* navigator.calculate_distance() -> float

## Interpreter:
* interpreter.logger -> logger
* interpreter.debug -> bool
* interpreter.nav -> Navigator
* interpreter.process_instructions_file(instructions_file: str) -> bool

