# Ascii PLOTTER for python 3 (APLOTTER3)

A stranger from the internet named Imri wrote this. You can [read about Imri at their website](https://www.algorithm.co.il/about-2/), see their [post about this code from some time in maybe 2007?](https://www.algorithm.co.il/ascii-plotter/), and [download a zipfile of the original source](http://www.algorithm.co.il/sitecode/aplotter.zip).

I ported it to Python3 so I could generate some documentation with plots in it, and thought I should share the updated version in case someone else finds it useful.


## How did I install this?

```sh
pip install aplotter3
```


## How do I use this?


```python
import aplotter3 as ap3
import numpy as np

x = np.sin(np.linspace(0, 6*np.pi, 100))
ap3.plot(x, x_size=60, y_size=15)
```

prints

```
  |
  +1  -\\               -\\               --\
  |  /  \\             /  \\             /   \
  | /    \             /    \            /    \
  | /     \           /     \           /     \
  |/      \           /      \          /      \
  |/       \         /       \         /       \
--+--------\--------/--------\---------/-------\---------+--
  +0        \       /         \       /         \     +99
  |         \      /          \      /           \      /
  |          \     /           \     /           \     /
  |          \    /            \    /             \    /
  |           \   /             \\  /             \\  /
  -1           --/               \-/               \-/
  |
```