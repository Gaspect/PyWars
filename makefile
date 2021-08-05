# help         Show this information.
.PHONY: help
help:
	cat makefile | grep -oP "^# \K(.*)"

# ‎‎
# ---------------------------------------------------------------------------
# The following commands must be run in the deploy environment.
# ---------------------------------------------------------------------------
# ‎‎

# format       Format all source code inplace using `black`.
.PHONY: format
format:
	black PyWars
# 

.PHONY: docs-prepare
docs-prepare: format
	python illiterate preset build

# docs         Compile and publish the documentation to Github.
.PHONY: docs-build
docs-build: docs-prepare
	mkdocs build

# gh-deploy    Deploy docs to Github Pages
.PHONY: docs-deploy
docs-deploy: docs-build
	mkdocs gh

