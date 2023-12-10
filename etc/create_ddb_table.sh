#!/usr/bin/env bash
set -e -o pipefail

# Mostly only useful for CI, see README for other localstack commands
hatch shell

awslocal dynamodb create-table \
  --table-name Distance \
  --attribute-definitions AttributeName=Name,AttributeType=S \
  --key-schema AttributeName=Name,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

awslocal dynamodb put-item \
  --table-name Distance \
  --item '{"Name": {"S":"Distance"}, "Distance": {"N": "0"}}'
