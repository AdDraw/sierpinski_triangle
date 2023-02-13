import math
import random as r

import matplotlib.pyplot as plt
import argparse

import time

from tabulate import tabulate

class Point:
    x = -1
    y = -1

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        return f"{self.x}x{self.y}"

    @property
    def l(self):
        return [self.x, self.y]


class RandomPoint(Point):
    def __init__(self, height: int, width: int, offset_x : int, offset_y: int) -> None:
        val_x = r.randint(0, height - 1) + offset_x
        val_y = r.randint(0, width - 1) + offset_y
        super().__init__(val_x, val_y)


class EqiTriangle:
    a = None
    b = None
    c = None

    def __init__(self, base_length, height, zero_point: Point) -> None:
        self.a = Point(
            zero_point.x,
            zero_point.y - int(base_length / 2),
        )
        self.b = Point(
            zero_point.x,
            zero_point.y + int(base_length / 2),
        )
        self.c = Point(zero_point.x + height, zero_point.y)

    @property
    def l(self):
        return [self.a.l, self.b.l, self.c.l]

    @property
    def points(self):
        return self.a, self.b, self.c


class Pair:
    a = None
    b = None

    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    @property
    def middle_point(self) -> Point:
        max_x = max(self.a.x, self.b.x)
        min_x = min(self.a.x, self.b.x)
        len_x = max_x - min_x

        max_y = max(self.a.y, self.b.y)
        min_y = min(self.a.y, self.b.y)
        len_y = max_y - min_y

        middle_point_x = int(len_x / 2) + min_x
        middle_point_y = int(len_y / 2) + min_y
        return Point(middle_point_x, middle_point_y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--points", default=100000, help="How many points should be drawn(def = 1000000)", type=int)
    parser.add_argument("-tal","--triangle-arm-length", default=1000, help="width & height of the array(def=10000)", type=int)
    parser.add_argument("--show", default=False, action="store_true", help="displays the figure with the triangle")
    parser.add_argument("--save", default=False, action="store_true", help="displays the figure with the triangle")
    args = parser.parse_args()
    print(args)
    t_arm_len = args.triangle_arm_length
    point_n = args.points

    # List to store prof times
    prof_times = []

    # Initialize the ZeroPoint (position of the middle of the base of the triangle)
    zp = Point(0, int(t_arm_len/2))
    print(f"ZeroPoint: {zp.l}")
    # Initialize the Triangle with equivalent arm lengths
    baselenght = int(0.9 * t_arm_len)
    t = EqiTriangle(baselenght, int(baselenght * math.sqrt(3) / 2), zp)
    print(f"Triangle:\n- Arm Length: {baselenght}\n- A pos(Left): {t.a.show()}\n- B pos(Right): {t.b.show()}\n- C pos(Top): {t.c.show()}")

    # Initialize the Random Point
    x = RandomPoint(math.ceil(0.02*t_arm_len), math.ceil(0.02*t_arm_len), zp.x, zp.y)
    print(f"RandomPoint position: {x.l}")

    # Initialize exisiting_points
    existing_points = list(t.points)
    existing_points.append(x)

    # Draw middle points
    middle_point_n = point_n
    s_time = time.time()
    for i in range(middle_point_n):
        point_a = existing_points[-1]
        point_b = r.sample(t.points, 1)[0]
        existing_points.append(Pair(point_a, point_b).middle_point)
    e_time = time.time()
    prof_times.append([f"draw_point_loop({point_n:.0e})", f"{(e_time - s_time):.2e}s"])

    # Convert Points into X,Y vectors
    xes = []
    ys = []
    s_time = time.time()
    xes = [p.x for p in existing_points]
    ys = [p.y for p in existing_points]
    e_time = time.time()
    prof_times.append([f"points to plot data loop", f"{(e_time - s_time):.2e}"])

    # Plot the sierpinski triangle
    s_time = time.time()
    plt.plot(ys, xes, marker="o", linewidth=0, markersize=0.1)
    plt.axis('off')
    e_time = time.time()
    prof_times.append([f"plot", f"{(e_time - s_time):.2e}"])

    # Print profiling
    print(f"\n{tabulate(prof_times, headers=['Profiling task', 'Time[s]'])}")

    # (opt) Save & show Sierpinski Triangle Plot
    if args.save:
      print("\nSaving to sierp_t.svg...")
      plt.savefig("sierp_t.svg", format="svg", backend="cairo", transparent=True)
    print("Save done")
    if args.show:
      plt.show()

