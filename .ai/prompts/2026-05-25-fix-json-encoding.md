# Goal

Fix JSON loading issues caused by UTF-8 BOM encoding.

Current error:

JSONDecodeError: Unexpected UTF-8 BOM

---

# Requirements

Refactor JSON loading utilities to properly support:
- UTF-8
- UTF-8 with BOM

Use:
encoding="utf-8-sig"

where appropriate.

---

# Architecture

Avoid repeating encoding fixes everywhere.

Create reusable JSON loading helper utilities if needed.

Suggested structure:

utils/
    json_loader.py

---

# Expected Result

JSON configuration files load correctly on Windows environments.