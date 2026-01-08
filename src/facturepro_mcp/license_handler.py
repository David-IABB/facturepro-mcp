"""License Handler - Pro Package Detection & Validation

Supports:
- Automatic Pro package detection
- License validation (Ed25519 signatures)
- Graceful fallback to Lite
"""

import os
import logging
import hashlib
from typing import Dict, Any
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

LICENSE_API_URL = "https://api.iabb.eu/v1/license/validate"

def validate_license(key: str) -> Dict[str, Any]:
    """Validate IABB license key

    Args:
        key: License key (format: IABB-XXXXX-XXXXX-XXXXX)

    Returns:
        {{
            "valid": bool,
            "reason": str,
            "expiry": datetime | None,
            "tier": "basic" | "pro" | "enterprise",
            "features": list[str]
        }}
    """

    # Format check
    if not key.startswith("IABB-"):
        return {"valid": False, "reason": "Invalid key format"}

    # TODO: Implement actual validation
    # Option 1: API call to IABB license server
    # Option 2: Ed25519 signature verification
    # Option 3: Local validation (offline mode)

    # Placeholder
    return {
        "valid": False,
        "reason": "License validation not implemented (demo mode)",
        "expiry": None,
        "tier": None,
        "features": []
    }

def check_pro_installed() -> bool:
    """Check if Pro package is installed"""

    try:
        import facturepro_core_pro
        return True
    except ImportError:
        return False

def get_license_from_env() -> str | None:
    """Get license key from environment"""

    return os.getenv("IABB_LICENSE_KEY") or os.getenv("IABB_LICENSE")

def cache_validation(result: Dict[str, Any], ttl_hours: int = 24):
    """Cache validation result locally"""

    # TODO: Implement file-based cache
    pass

def load_cached_validation() -> Dict[str, Any] | None:
    """Load cached validation (for offline mode)"""

    # TODO: Implement
    return None
