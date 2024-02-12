#!/bin/bash

# Stop on the first sign of trouble
set -e

echo "Fetching access token for introspection..."
SYSAIR_INTROSPECTION_TOKEN=$(python codegen/get_token.py)

echo "Token fetched: $SYSAIR_INTROSPECTION_TOKEN"
echo "Running code generation..."

export SYSAIR_INTROSPECTION_TOKEN

# Generate the GraphQL SDL (codegen/schema.graphql)
poetry run ariadne-codegen graphqlschema

# Generate the Python code (pysysair/graphql)
poetry run ariadne-codegen

echo "Code generation complete!"
