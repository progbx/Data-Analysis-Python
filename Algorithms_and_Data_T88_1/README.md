__Task description__

Given a list of points on a plane, sort them in descending order of the points' distance from the origin. If two points are equally distant from the origin, return the leftmost one first. If two points are equally distant from the origin and lie on the same vertical, return the bottom one first.
Each point is represented as a pair of coordinates _(x, y)_.

<br>

__Test data sets examples__

| № | Input data | Expected output |
|----------|----------|----------|
| 1    | [(2, 2), (4, 3), (0, 0), (1, 0)]    | [(4, 3), (2, 2), (1, 0), (0, 0)]   |
| 2    | [(0, 1), (0, -1), (-1, 0), (0, 0)] | [(-1, 0), (0, -1), (0, 1), (0, 0)]    |