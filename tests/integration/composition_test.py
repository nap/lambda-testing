__author__ = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"
import math
import unittest

import pytest

from calculation import distance, eventtype


class TestComposition(unittest.TestCase):
    @pytest.mark.integration
    def test_get_distance_from_event_noop_enum(self) -> None:
        result: dict = distance._get_distance_from_event(
            {"coordinate": {"x": 1, "y": 1}, "type": eventtype.EventType.NOOP}
        )
        calculation: float = math.sqrt(1**2 + 1**2)
        self.assertAlmostEqual(calculation, result["distance"])

    def test_get_distance_from_event_noop_str(self) -> None:
        result: dict = distance._get_distance_from_event({"coordinate": {"x": 1, "y": 1}, "type": "noop"})
        calculation: float = math.sqrt(1**2 + 1**2)
        self.assertAlmostEqual(calculation, result["distance"])

    @pytest.mark.integration
    def test_should_increment_unknown(self) -> None:
        event: dict = {"coordinate": {"x": 1, "y": 1}, "type": "unknown"}
        with pytest.raises(ValueError):
            distance._should_increment(event)
