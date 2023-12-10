__author__: str = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"

import os

import boto3
from loguru import logger as log
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table
from mypy_boto3_dynamodb.type_defs import TableAttributeValueTypeDef, UpdateItemOutputTableTypeDef

from calculation.coordinate import Coordinate
from calculation.eventtype import EventType

__DYNAMODB_ENDPOINT_URL__: None | str = None
if "AWS_EXECUTION_ENV" not in os.environ:
    # Unless the script is being used in aws, use localstack.
    __DYNAMODB_ENDPOINT_URL__ = "https://localhost.localstack.cloud:4566"

__DYNAMODB_TABLE__: str = "Distance"
__DYNAMODB_FIELD__: str = "Distance"


def _get_dynamodb_table(table: str) -> Table:
    ddb: DynamoDBServiceResource = boto3.resource("dynamodb", endpoint_url=__DYNAMODB_ENDPOINT_URL__)
    return ddb.Table(table)


def _update_increment_counter() -> UpdateItemOutputTableTypeDef:
    table: Table = _get_dynamodb_table(__DYNAMODB_TABLE__)
    return table.update_item(
        Key={"Name": __DYNAMODB_TABLE__},
        UpdateExpression=f"ADD {__DYNAMODB_FIELD__} :val",
        ExpressionAttributeValues={":val": 1},
        ReturnValues="UPDATED_NEW",
    )


def _parse_operation_result(result: UpdateItemOutputTableTypeDef) -> TableAttributeValueTypeDef:
    return result["Attributes"]["Distance"]


def _parse_coordinate(event: dict) -> Coordinate:
    coordinates: dict = event["coordinate"]
    return Coordinate(**coordinates)


def _parse_event(event: str | EventType) -> EventType:
    try:
        return EventType(event.lower())

    except ValueError as ve:
        msg: str = f"event type for '{event}' is not supported"
        log.warning(msg)
        raise ValueError(msg) from ve


def _should_increment(raw_event: dict) -> bool:
    try:
        log.info(f"event type is {raw_event['type']}")
        event: EventType = _parse_event(raw_event["type"])
        if event in [EventType.NOOP, EventType.FAKE]:
            return False

        if event == EventType.PERSIST:
            return True

    except KeyError:
        log.warning("was unable to get event type from event, event is malformed")
        return False

    log.critical("was unable to get event type but exception was not catched, we can't recover")
    return False


def _get_distance_from_event(event: dict) -> dict:
    coordinate: Coordinate = _parse_coordinate(event)
    log.info(f"got {coordinate} from event")

    distance: float = coordinate.calculate()
    log.info(f"distance from coordinate ({coordinate.x}, {coordinate.y}) is {distance}")

    if _should_increment(event):
        log.debug(f"got real event for coordinate {coordinate}")
        result: UpdateItemOutputTableTypeDef = _update_increment_counter()
        log.debug(f"hit for counter: {_parse_operation_result(result)}")

    return {"distance": distance}


def lambda_handler(event: dict, context: dict) -> dict:
    log.debug(f"received event '{event}' with context '{context}'.")
    return _get_distance_from_event(event["detail"])


if __name__ == "__main__":
    distance: dict = lambda_handler({"detail": {"coordinate": {"x": "1", "y": "1"}, "type": "noop"}}, {})
    log.debug(f"computed distance is: {distance}")
