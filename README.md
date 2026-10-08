### Created by Ben Collingridge.

# What is Collatz Conjecture?
>Collatz Conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.  

_From [https://en.wikipedia.org/wiki/Collatz_conjecture]_

## What are the two simple arithmetic operations?
- If positive integer _n_ is even, do _n / 2_.
- If positive integer _n_ is odd, do _3n + 1_.
> With enough repetition, do all positive integers converge to 1?  

_From [https://en.wikipedia.org/wiki/Collatz_conjecture]_

## Some basic history.
- Named after the mathematician Lothar Collatz.
- Introduced the idea in 1937, two years after receiving his doctorate.
> The sequence of numbers is sometimes referred to as the hailstone sequence, hailstone numbers, or hailstone numerals (because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as wondrous numbers.  

_From [https://en.wikipedia.org/wiki/Collatz_conjecture]_

# How do I run the program?
- Install **matplotlib** if not already installed. This can be done (but not limited to) using:
> pip install matplotlib  

**OR**  

> py -m pip install matplotlib  

## main.py
- Choose the plot mode.
  - Set _mode_ to "d" to run the program for a definite amount of steps (also known as the _**stopping time**).
  - Set _mode_ to "i" to run the program until _n_ converges to 1 (indefinite).
  - Set _mode_ to "b" to plot both definite and indefinite modes starting at the same number.
- Choose the starting number (defined by _start_) for _n_.
  - By default, this is a random positive integer between 1 and 100, although this can be set to a definite positive integer, or the maximum random value can be increased or decreased.
- Choose the number of definite steps (_definite_steps_) if you are running in mode "d" or "b".
  - As mentioned previously, this is defaulted to 200 steps.

## tree_vis.py
- Install **pygame** if not already installed. This can be done (but not limited to) using:
> pip install pygame  

**OR**  

> py -m pip install pygame  
- Choose the number of runs (defined by _runs_). This controls how many chains of numbers converging to one are drawn.
- Adjust any starting number parametres.
  - I have found that the sort of sweet spot is 5 runs with a random integer between 1 and 150.
  - The number of runs seems to affect the detail in one spot, whereas the random starting integer affects the detail of the "plant".
  - Increasing either values decreases the chance of good result.
 
# Analysis of main.py
The starting number is defined by:
```py
import random
start = random.randint(1, 100)
```

Finding the next value of _n_ is very simple:
```py
def collatz(n):
  if n % 2 == 0:
    return n / 2
  else:
    return (n * 3) + 1
```

To calculate the definite data:
```py
n = start
for i in range(1, definite_steps + 1):
  n = int(collatz(n))
  x.append(i)
  y.append(n)
```

To calculate the indefinite data:
```py
n = start
i = 0
while n != 1:
  i += 1
  n = int(collatz(n))
  x.append(i)
  y.append(n)
```

After the _x_ and _y_ datasets are full, we can plot the data using another function, which utilises matplotlib's plot() function:
```py
import matplotlib.pyplot as plt
def plot_data(x_data, y_data, plot_title, steps, x_label="X-axis", y_label="Y-axis"):
  plt.plot(x_data, y_data, marker="o", markerfacecolor="red", markersize=5)
  plt.xlim(1, steps)
  plt.ylim(1, max(y_data))
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.title(plot_title)
  plt.show()
```

If we want to plot the data for both definite and indefinite, we need to create duplicates of _x_, _y_, _n_, and _i_, and then use matplotlib slightly differently:
```py
# definite
n = start
for i in range(1, definite_steps + 1):
  n = int(collatz(n))
  x.append(i)
  y.append(n)

# indefinite
n2 = start
i2 = 0
while n2 != 1:
  i2 += 1
  n2 = int(collatz(n2))
  x2.append(i2)
  y2.append(n2)

# plot
plt.plot(x, y, marker="o", markerfacecolor="red", markersize=5, label="Definite")
plt.plot(x2, y2, marker="o", markerfacecolor="green", markersize=5, label="Indefinite")
plt.xlim(1, definite_steps)
plt.ylim(1, max(y))
plt.xlabel("Steps")
plt.ylabel(f"n - Start: {start}")
plt.title("Collatz Conjecture - Visualised")
plt.legend()
plt.show()
```
## Results
<img width="971" height="687" alt="image" src="https://github.com/user-attachments/assets/0aa25bd5-8b81-4723-8e56-6b41782444c7" />

_Typical result for "both"._

<img width="999" height="761" alt="image" src="https://github.com/user-attachments/assets/0e87265c-cd07-42da-b5e7-0d6cf9d17e38" />

_From a lower starting number, we can more easily see the 4-2-1 loop which occurs after n has initially converged to 1._

<img width="1000" height="701" alt="image" src="https://github.com/user-attachments/assets/2a923fc0-f9a6-4888-92fc-e179a7427650" />

_The results are sometimes a little bit more interesting._

# Analysis of tree_vis.py
This code uses _pygame_ to visualise the tree or plant form which I have noticed comes from using this conjecture. It uses the exact same process to calculate the sequence of numbers according to the conjecture. However, the data is stored as an array holding two 2-dimensional vectors. These vectors store information on its _x_ and _y_ values (origin) along with its destination coordinates. The origin is simply the last item's destination. The destination is then determined by taking the previous item's _x_ and moving it left or right depending on if it's even or odd, respectively. The _y_ is that of the last item's but moving it up by an arbitrary value.

The code to calculate this data and store it is as follows:
```py
trunk = [pg.Vector2(screen.get_width() / 2, screen.data.append(trunk)]
n = random.randint(1, 150)
i = 0
while n != 1:
  i += 1
  n = int(collatz(n))
  mult = 0
  if is_even(n):
    mult -= 1
  else:
    mult = 1
  data.append([data[i - 1][1], pg.Vector2(data[i - 1][1].x + mult * n, data[i - 1][1].y - 30)])
```

By nesting this in:
```py
for i in range(runs)
```
We can do this algorithm multiple times to create more runs and, therefore, more detail. To render this image based on the coordinates we can do:
```py
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

  screen.fill("black")

  for val in data:
    pg.draw.line(screen, "white", val[0], val[1], 2)

  pg.display.update()
  pg.display.flip()
  clock.tick(144)

pg.quit()
```

## Results
We get some interesting results which almost resemble trees or plants. It's important to note that increasing the number of runs and the initial starting number will decrease the chance of a clean result, but will increase the chancee of a clean result looking more interesting. This will also come at a cost of processing.

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/5dc83dc3-377b-4e25-bd47-fe2059f21942" />

_We get some odd results like this which don't exactly resemble anything._

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/bb2cce13-638d-4971-99bf-5f8018fbac16" />

_And we also get messy results like this which somewhat resemble a plant's central structure._

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/7253f6c3-ca4c-4744-a4a5-6f4d67273e64" />

_Dead plant?_

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/22d71d99-d2ca-44ce-b265-82b9f514f86c" />

_But we also get more structured results like this._

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/00c80bc3-ce61-4286-8a2d-1c50b4e277a9" />
<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/8a088834-6b17-4b2a-9995-66950c0cd987" />

_Almost looks like a fern leaf._

By decreasing the runs, we get less detail, and increasing the starting number produces more variation (generally):
<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/85dcba23-d61e-46ae-98a5-24ca79db47bc" />

_start = 50, runs = 1_

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/5f54ac85-d171-4c65-9141-58c0fd0e985e" />

_start = 79, runs = 1_

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/2156a0e9-78b5-469e-801b-542f0f533806" />

_start = randint(1, 150), runs = 50_

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/367f4b24-92ca-450c-8bab-55d5d2a952b5" />

_start = randint(1, 50), runs = 50_

<img width="1282" height="759" alt="image" src="https://github.com/user-attachments/assets/2a5920c1-23e6-4eb1-9252-be6bcb607204" />

_start = randint(1, 150), runs = 200_
