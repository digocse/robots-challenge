# robots-challenge

## About
This application has been created in order to explore Mars territory at its most by using robots!
It is possible to feed the application with the size of the grid that you would like to explore, robots coordinates and instructions. Enjoy!

## Prerequisites
Install Python 3 and pyenv.

- Install [pyenv](https://github.com/pyenv/pyenv):

    `curl https://pyenv.run | bash`

    Caveat:
    - Remember to add the final lines printed by the previous command in your rc file (.bashrc/.zshrc)

### Setup environment

```bash
cd path/to/robots-challenge/
pyenv install 3.6.12
pyenv virtualenv 3.6.12 robots
```

Activate the virtualenv:

```bash
source activate robots
```

Install dependencies locally (required to run tests):

    pip install -r requirements.txt
    py.test -s --verbose


## Run the app
```bash
python main.py
```

Fill the file `robots_guide.in.md` with the proper input data in the following format:

```bash
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
```

Sample output for the above input:
```bash
*** Welcome to the Mars Robots Guide! ***

Here are the computed outputs:

(1, 1, 'E')
(3, 3, 'N') LOST
(2, 3, 'S')
```

The first line of input is the upper-right coordinates of the rectangular world, the lower-left coordinates are assumed to be 0, 0.
The remaining input consists of a sequence of robot positions and instructions (two lines per robot). A position consists of two integers specifying the initial coordinates of the robot and an orientation (N, S, E, W), all separated by whitespace on one line. A robot instruction is a string of the letters “L”, “R”, and “F” on one line.


## Testing
Install the necessary dependencies and run the tests:

    pip install -r requirements.txt
    py.test -s --verbose


## Coverage
To perform the test coverage analysis, run the command:
    `py.test -xs --cov . --cov-report=term .`
