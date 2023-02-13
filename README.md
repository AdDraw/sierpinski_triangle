### Sierpinski Triangle

> Wiki: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle

Achieved using [Chaos Game](https://en.wikipedia.org/wiki/Chaos_game) method described on Wikipedia.

**Steps:**

- Draw 3 points of the eqiTriangle`p0,p1,p2`
- draw a point`p3` on random (I have constrained it a fair bit)
- now draw the next point`p4` as a point at half the distance between`p3` and a single point of the triangle that was chosen at random`p0,p1,p2`
- continue but next point`p5` is drawn at half the distance of a pair of points`p4 and random(p0,p1,p2)`
- repeat until satisfactory


**Result of** `sierpinski.py`:

![sierp svg](sierp_t.svg)


![](sierp_t.vsg)
