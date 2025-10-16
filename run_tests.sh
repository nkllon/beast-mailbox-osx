#!/bin/bash
# Simple test runner for beast-mailbox-osx
# Works without pytest installed

set -e  # Exit on error

echo "========================================"
echo "Running beast-mailbox-osx Tests"
echo "========================================"
echo ""

cd "$(dirname "$0")"

# Check if on macOS
if [[ "$OSNAME" != "Darwin" ]]; then
    echo "⚠️  Warning: These tests are designed for macOS"
fi

# Check if package is installed
echo "Checking installation..."
python3 -c "import beast_mailbox_osx" 2>/dev/null || {
    echo "❌ Package not installed. Installing..."
    python3 -m pip install -e . --quiet
}
echo "✓ Package installed"
echo ""

# Run tests
echo "Running test suite..."
echo ""

for test_file in tests/test_*.py; do
    echo "Running $(basename "$test_file")..."
    python3 "$test_file"
    echo ""
done

echo "========================================"
echo "All tests completed successfully! ✅"
echo "========================================"

