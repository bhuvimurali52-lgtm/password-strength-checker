#!/usr/bin/env bash
set -euo pipefail

# Stdlib-only Python project: verify the module imports after checkout.
python3 -c "from password_checker import PasswordStrengthChecker"
