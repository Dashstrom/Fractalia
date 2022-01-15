# Fractalia
Tkinter application for generate landscapes composed of fractals.


## Fractal used
- Barnsley fern
- Fractal Tree
- Julia
- Diamond-square algorithm

# Install
```
git clone https://github.com/Dashstrom/Fractalia.git
pip install .
python3 -m fractalia
```
## Remove
```
pip uninstall fractalia
```

## Commands

```
usage: python3 -m fractalia [-h] [-s SEED] [-n NUMBER]

Tkinter application for generate landscapes composed of fractals.

options:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  Seed for random generator
  -n NUMBER, --number NUMBER
                        Generate N images in directory named 'out'
```

## Examples$
### Commande line
- `python3 -m fractalia` : Open an Tkinter App
- `python3 -m fractalia -s 42` : Open Tkinter App with seed 78
- `python3 -m fractalia -n 7` : Generate 7 images

### As import
```python
from fractalia import drawing

img = drawing()
img.show()
```
# Results

![Landscape of seed 461170130558899640](https://raw.githubusercontent.com/Dashstrom/Fractalia/main/docs/exemples/461170130558899640.png "461170130558899640")
![Landscape of seed 2350265372157330445](https://raw.githubusercontent.com/Dashstrom/Fractalia/main/docs/exemples/2350265372157330445.png "2350265372157330445")
![Landscape of seed 4402446516260078720](https://raw.githubusercontent.com/Dashstrom/Fractalia/main/docs/exemples/4402446516260078720.png "4402446516260078720")
![Landscape of seed 6123730475364912831](https://raw.githubusercontent.com/Dashstrom/Fractalia/main/docs/exemples/6123730475364912831.png "6123730475364912831")