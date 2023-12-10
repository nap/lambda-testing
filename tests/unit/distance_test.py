__author__ = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"
import unittest

import pytest

from calculation import distance
from calculation.coordinate import Coordinate
from calculation.eventtype import EventType


class TestLambda(unittest.TestCase):
    @pytest.mark.unit
    def test_parse_coordinate_type(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "1"}, "type": "noop"}
        self.assertIsInstance(distance._parse_coordinate(event), Coordinate)

    @pytest.mark.unit
    def test_parse_coordinate_x_int(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "2"}, "type": "noop"}
        self.assertIsInstance(distance._parse_coordinate(event).x, int)

    @pytest.mark.unit
    def test_parse_coordinate_y_int(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "2"}, "type": "noop"}
        self.assertIsInstance(distance._parse_coordinate(event).y, int)

    @pytest.mark.unit
    def test_should_increment_noop(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "1"}, "type": "noop"}
        self.assertFalse(distance._should_increment(event))

    @pytest.mark.unit
    def test_should_increment_persist(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "1"}, "type": "persist"}
        self.assertTrue(distance._should_increment(event))

    @pytest.mark.unit
    def test_should_increment_unknown(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "1"}, "type": "unknown"}
        with pytest.raises(ValueError):
            distance._should_increment(event)

    @pytest.mark.unit
    def test_should_increment_undef(self) -> None:
        event: dict = {"coordinate": {"x": "1", "y": "1"}}
        self.assertFalse(distance._should_increment(event))

    @pytest.mark.unit
    def test_parse_event_noop(self) -> None:
        event: str = "NOoP"
        self.assertEqual(EventType.NOOP, distance._parse_event(event))

    @pytest.mark.unit
    def test_parse_event_persist(self) -> None:
        event: str = "PerSiSt"
        self.assertEqual(EventType.PERSIST, distance._parse_event(event))

    @pytest.mark.unit
    def test_parse_event_unknown(self) -> None:
        event: str = "unknown"
        with pytest.raises(ValueError):
            distance._parse_event(event)

    @pytest.mark.unit
    def test_parse_event_undef(self) -> None:
        event: str = ""
        with pytest.raises(ValueError):
            distance._parse_event(event)
