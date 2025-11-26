# awiesm.pycmor_helpers

AWI-ESM helpers for pycmor - utilities for working with pycmor in the AWI-ESM modeling framework.

## Installation

This project uses [pixi](https://pixi.sh) for dependency management.

### Using pixi

```bash
# Install dependencies
pixi install

# Run tests
pixi run test

# Run tests with coverage
pixi run test-cov

# Format code
pixi run format

# Lint code
pixi run lint

# Type check
pixi run typecheck
```

### Traditional installation

```bash
pip install -e .
```

## Development

The project uses:
- **xarray** for n-dimensional labeled arrays
- **pycmor** for CMOR operations
- **pytest** for testing
- **black** for code formatting
- **ruff** for linting
- **mypy** for type checking

## Project Structure

```
awiesm.pycmor_helpers/
├── src/
│   └── awiesm/
│       └── pycmor_helpers/
│           └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_basic.py
├── docs/
├── pyproject.toml
└── README.md
```

## Using in PyCMOR

Once you have defined your step, you can include in in a pipeline:

```yaml
pipelines:
  - name: custom-pipeline
    steps:
        - "pycmor.std_lib.generic.get_variable"
        - "pycmor.std_lib.timeaverage.timeavg"
        - "awiesm.pycmor_helpers.oifs.sample_step" 
        - "pycmor.std_lib.units.handle_unit_conversion"
        - "pycmor.std_lib.global_attributes.set_global_attributes"
        - "pycmor.std_lib.variable_attributes.set_variable_attributes"

```

## License

MIT
