import cv2
import numpy as np
from matplotlib import pyplot as plt


class DiceCOF:
    def __init__(self, Object) -> None:
        self.Object = Object
        pass

    def dice_coefficient(self, target):
        # Convert the inputs to sets
        x = set(self.Object)
        y = set(target)
        # Calculate the intersection and the union of the sets
        intersection = x.intersection(y)
        union = x.union(y)
        # Calculate the Dice coefficient using the formula
        dsc = (2 * len(intersection)) / (len(x) + len(y))
        # Return the Dice coefficient
        return dsc
