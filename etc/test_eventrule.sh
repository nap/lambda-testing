#!/usr/bin/env bash
set -e -o pipefail

hatch shell

awslocal events \
  test-event-pattern \
  --event-pattern '{
    "source": [
      "custom.cli"
    ],
    "detail-type": [
      "coordinate"
    ]
  }' \
  --event '{
    "version": 0,
    "account": "123456789123",
    "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
    "detail-type": "coordinate",
    "source": "custom.cli",
    "time": "2017-12-22T18:43:48Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
      "coordinate": {"x": 5, "y": 5},
      "type": "persist"
    }
  }'
