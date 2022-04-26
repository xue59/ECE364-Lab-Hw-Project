#! /usr/bin/env python3.4
#
#$Author: ee364b13 $
#$Date: 2016-02-25 22:02:04 -0500 (Thu, 25 Feb 2016) $
#$Revision: 88930 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab07/points.py $
#$Id: points.py 88930 2016-02-26 03:02:04Z ee364b13 $

import math

class PointND:
    def __init__(self, *args):
        for arg in args:
            if not isinstance(arg, float):
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.n = len(args)
        self.t = args

    def __str__(self):
        string = "("
        ind = 0
        for i in self.t:
            if ind == self.n - 1:
                string += "%.2f" % i + ")"
            else:
                string += "%.2f" % i + ", "
            ind += 1
        return string

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        distance_square = 0
        for x, y in zip(self.t, other.t):
            distance_square += (x-y)**2
        distance = math.sqrt(distance_square)
        return distance

    def nearestPoint(self, points):
        if len(points) == 0:
            raise ValueError("Input cannot be empty.")
        min_pt = points[0]
        min_dist = self.distanceFrom(points[0])
        for pt in points:
            if self.distanceFrom(pt) < min_dist:
                min_dist = self.distanceFrom(pt)
                min_pt = pt
        return min_pt

    def clone(self):
        return PointND(*self.t)

    def __add__(self, other):
        if isinstance(other, float):
            return PointND(*tuple(x + other for x in self.t))
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return PointND(*tuple(x + y for x,y in zip(self.t, other.t)))

    def __sub__(self, other):
        if isinstance(other, float):
            return PointND(*tuple(x - other for x in self.t))
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return PointND(*tuple(x - y for x,y in zip(self.t, other.t)))

    def __radd__(self, other):
        if isinstance(other, float):
            return PointND(*tuple(x + other for x in self.t))
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return PointND(*tuple(x + y for x,y in zip(self.t, other.t)))

    def __rsub__(self, other):
        if isinstance(other, float):
            return PointND(*tuple(x - other for x in self.t))
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return PointND(*tuple(x - y for x,y in zip(self.t, other.t)))

    def __mul__(self, other):
        return PointND(*tuple(x * other for x in self.t))

    def __truediv__(self, other):
        return PointND(*tuple(x / other for x in self.t))

    def __rmul__(self, other):
        return PointND(*tuple(x * other for x in self.t))

    def __rtruediv__(self, other):
        return PointND(*tuple(x / other for x in self.t))

    def __neg__(self):
        return PointND(*tuple(-x for x in self.t))

    def __getitem__(self, k):
        return self.t[k]

    def __eq__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        for x, y in zip(self.t, other.t):
            if x != y:
                return False
        return True

    def __ne__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        for x, y in zip(self.t, other.t):
            if x == y:
                return False
        return True

    def __gt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        x_tot = 0
        y_tot = 0
        for x, y in zip(self.t, other.t):
            x_tot += x**2
            y_tot += y**2
        return x_tot > y_tot

    def __ge__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        x_tot = 0
        y_tot = 0
        for x, y in zip(self.t, other.t):
            x_tot += x**2
            y_tot += y**2
        return x_tot >= y_tot

    def __lt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        x_tot = 0
        y_tot = 0
        for x, y in zip(self.t, other.t):
            x_tot += x**2
            y_tot += y**2
        return x_tot < y_tot

    def __le__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        x_tot = 0
        y_tot = 0
        for x, y in zip(self.t, other.t):
            x_tot += x**2
            y_tot += y**2
        return x_tot <= y_tot

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        if not (isinstance(x, float) and isinstance(y, float) and isinstance(z, float)):
            raise ValueError("Cannot instantiate an object with non-float values.")
        self.x = x
        self.y = y
        self.z = z
        self.t = (x, y, z)
        self.n = 3


class PointSet:
    def __init__(self, **kwargs):
        if kwargs == None:
            self.points = set()
            self.n = 0
        else:
            if "pointList" in kwargs:
                if not kwargs["pointList"]:
                    raise ValueError("'pointList' input parameter cannot be empty.")
                self.points = set(kwargs["pointList"])
                self.n = kwargs["pointList"][0].n
                for pt in kwargs["pointList"]:
                    if pt.n != self.n:
                        raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
            else:
                raise KeyError("'pointList' input parameter not found.")

    def addPoint(self, p):
        if p.n != self.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        self.points.add(p)

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        list_of_pts = list(self.points)
        mint = list(list_of_pts[0].t)
        maxt = list(list_of_pts[0].t)
        for pt in list_of_pts:
            for i in range(0, self.n):
                if pt.t[i] < mint[i]:
                    mint[i] = pt.t[i]
                if pt.t[i] > maxt[i]:
                    maxt[i] = pt.t[i]
        minPoint = PointND(*tuple(mint))
        maxPoint = PointND(*tuple(maxt))
        return (minPoint, maxPoint)

    def computeNearestNeighbors(self, otherPointSet):
        result = []
        for u in self.points:
            nearest = list(otherPointSet.points)[0]
            nearest_dist = u.distanceFrom(nearest)
            for v in otherPointSet.points:
                if u.distanceFrom(v) < nearest_dist:
                    nearest = v
                    nearest_dist = u.distanceFrom(v)
            result.append((u,nearest))
        return result

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        self.points.add(other)
        return self

    def __sub__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        if other in self.points:
            self.points.remove(other)
        return self

    def __contains__(self, item):
        return item in self.points

if __name__ == "__main__":
    pass