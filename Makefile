
# Makefile

# Displays all make targets in a column format
.PHONY: help
help: ## displays all available make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Installs all dependencies and sets up pre-commit
.PHONY: install
install: ## installs all dependencies
	@poetry install
	@poetry run pre-commit install --install-hooks

# Installs only dev dependencies and sets up pre-commit
.PHONY: install-dev
install-dev: ## installs only dev dependencies
	@poetry install --dev-only
	@poetry run pre-commit install --install-hooks
