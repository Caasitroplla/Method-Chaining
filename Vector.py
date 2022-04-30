from dataclasses import dataclass
import numpy as np


@dataclass
class Vector:
    x: float
    y: float
    z: float

    def normalised(self):
        x, y, z = self.x, self.y, self.z
        norm = np.sqrt(x**2 + y**2 + z**2)
        return type(self)(x/norm, y/norm, z/norm)

    def reflected(self):
        return type(self)(-self.x, -self.y, -self.z)

def main():
    p = Vector(1., 2., 3.)
    q = p.reflected().normalised()
    print(p)
    print(q)

main()