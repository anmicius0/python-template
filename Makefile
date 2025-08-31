
UV ?= uv

.PHONY: install dev lint clean

# Install project dependencies into uv-managed environment
install:
	$(UV) sync

# Install development extras (if any) using uv
dev:
	$(UV) sync --dev

# Run linter inside the uv-managed environment
lint:
	$(UV) run flake8 src || true

clean:
	rm -rf build dist *.egg-info
