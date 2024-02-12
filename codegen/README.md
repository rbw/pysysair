# GraphQL Codegen

This directory contains code for generating a low-level library for interacting with the Systemair GraphQL API in `pysysair.graphql`.

It requires `SYSTEMAIR_AUTH_EMAIL` and `SYSTEMAIR_AUTH_PASSWORD` to be set in order to work.

- gen_code.sh: Generates Python code for Interacting with the Systemair GraphQL API. Also, this script creates a copy of the introspected schema (schema.graphql).
- get_token.py: Wrapper for obtaining an access token using Resource Owner Password Flow with OIDC
- queries.graphql: GraphQL queries (manually maintained) for generating client methods in `pysysair.graphql`
- schema.graphql: Copy of the introspected schema that was used for generating the Python code in `pysysair.graphql`
