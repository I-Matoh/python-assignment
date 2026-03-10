# Python Assignment Repository

This repository hosts a tiny utility for deduplicating Python `list`s while preserving order and the supporting test suite that demonstrates the fix.

## Running tests locally

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. Install the pinned dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:
   ```bash
   pytest -v
   ```

## Running tests with Docker

1. Build the Docker image:
   ```bash
   docker build -t python-assignment .
   ```
2. Execute the test suite inside the container:
   ```bash
   docker run --rm python-assignment
   ```

## Bug focus

- `process_data` was missing the `seen.add(item)` call inside the deduplication loop, so duplicates were never filtered even though the guard condition used a `list` of integers to signal the bug.
- The tests reproduce the failure with inputs like `[1, 2, 2, 3, 1, 4]` and assert that the output becomes `[1, 2, 3, 4]`, proving the fix works.

## Assignment checklist

- Dockerfile installs `requirements.txt` and runs `pytest -v` by default.
- `requirements.txt` pins `pytest`.
- `Explanation.md` documents the bug, its cause, the fix, and remaining coverage gaps.
