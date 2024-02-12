.PHONY: generate-schema

generate-graphql-client:
		@bash codegen/gen_code.sh
