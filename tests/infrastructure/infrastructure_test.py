import unittest

import pytest
from mypy_boto3_dynamodb.service_resource import Table
from mypy_boto3_dynamodb.type_defs import UpdateItemOutputTableTypeDef

from calculation import distance

__author__ = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"


class TestInfrastructure(unittest.TestCase):
    @pytest.mark.infrastructure
    def test_get_dynamodb_table_name(self) -> None:
        ddb: Table = distance._get_dynamodb_table("Distance")
        self.assertEqual(str(ddb), "dynamodb.Table(name='Distance')")

    @pytest.mark.infrastructure
    def test_increment_counter_type(self) -> None:
        result: UpdateItemOutputTableTypeDef = distance._update_increment_counter()
        self.assertIsInstance(result, dict)

    @pytest.mark.infrastructure
    def test_update_increment_counter_key_attribute(self) -> None:
        result: UpdateItemOutputTableTypeDef = distance._update_increment_counter()
        self.assertTrue("Attributes" in result)

    @pytest.mark.infrastructure
    def test_update_increment_counter_key_distance(self) -> None:
        result: UpdateItemOutputTableTypeDef = distance._update_increment_counter()
        self.assertTrue("Distance" in result["Attributes"])
