__author__ = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"
import math
import unittest

import pytest

from calculation import coordinate


class TestCoordinate(unittest.TestCase):
    @pytest.mark.unit
    def test_calculation(self) -> None:
        self.assertEqual(math.sqrt(1**2 + 1**2), coordinate.Coordinate(1, 1).calculate())

    @pytest.mark.unit
    def test_str(self) -> None:
        self.assertEqual("Coordinate(1, 1)", str(coordinate.Coordinate(1, 1)))

    @pytest.mark.unit
    def test_coordinate_x(self) -> None:
        self.assertEqual(1, coordinate.Coordinate(1, 2).x)

    @pytest.mark.unit
    def test_coordinate_y(self) -> None:
        self.assertEqual(2, coordinate.Coordinate(1, 2).y)

    @pytest.mark.unit
    def test_coordinate_unpack(self) -> None:
        coord: dict = {"x": 1, "y": 2}
        self.assertEqual(coord["y"], coordinate.Coordinate(**coord).y)
