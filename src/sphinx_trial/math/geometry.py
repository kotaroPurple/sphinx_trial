"""Geometry calculations for basic shapes."""

import math
from typing import Union

Number = Union[int, float]


class Circle:
    """A circle with radius-based calculations."""

    def __init__(self, radius: Number) -> None:
        """Initialize a circle with given radius.
        
        Args:
            radius: Circle radius
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        """Calculate circle area.
        
        Returns:
            Area of the circle
        """
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """Calculate circle circumference.
        
        Returns:
            Circumference of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle:
    """A rectangle with width and height."""

    def __init__(self, width: Number, height: Number) -> None:
        """Initialize a rectangle with given dimensions.
        
        Args:
            width: Rectangle width
            height: Rectangle height
            
        Raises:
            ValueError: If width or height is negative
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width = width
        self.height = height

    def area(self) -> Number:
        """Calculate rectangle area.
        
        Returns:
            Area of the rectangle
        """
        return self.width * self.height

    def perimeter(self) -> Number:
        """Calculate rectangle perimeter.
        
        Returns:
            Perimeter of the rectangle
        """
        return 2 * (self.width + self.height)