"""FacturePro MCP Server - Public Interface

Basic version (free): ["PDF parsing", "Basic validation", "Format conversion"]
Pro version (€2,500/an): ["Signal Loop optimization", "Peppol Access Point", "Auto-repair", "Batch processing", "Real-time compliance checks"]

Install Basic:
    pip install facturepro_mcp

Install Pro:
    pip install facturepro_mcp facturepro-core-pro
    # Requires IABB license key

License: MIT (public package)
Copyright © 2026 IA Business Booster
"""

import os
import logging
from typing import Any, Optional
from trycast import to_importable

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    raise ImportError(
        "MCP SDK not installed. Install with: pip install mcp"
    )

# Try to import Pro engine (optional dependency)
try:
    from facturepro_core_pro import ProEngine
    PRO_AVAILABLE = True
except ImportError:
    PRO_AVAILABLE = False
    ProEngine = None

# Import Lite engine (always available)
from .lite_engine import LiteEngine

# License validation
from .license_handler import validate_license

logger = logging.getLogger(__name__)

class FactureProServer:
    """Main server with automatic Basic/Pro detection"""

    def __init__(self):
        self.server = Server("facturepro_mcp")
        self.license_valid = False
        self.engine = None
        self._init_engine()

    def _init_engine(self):
        """Initialize Lite or Pro engine based on license"""

        if PRO_AVAILABLE:
            logger.info("🔧 Pro package detected, validating license...")
            key = os.getenv("IABB_LICENSE_KEY")
            if key:
                validation = validate_license(key)
                if validation["valid"]:
                    self.license_valid = True
                    self.engine = ProEngine()
                    logger.info("✅ FacturePro PRO engine activated")
                    return
                else:
                    logger.warning("❌ Invalid license: %s", validation.get('reason', 'Unknown error'))
            else:
                logger.warning("⚠️  No IABB_LICENSE_KEY found")
        else:
            logger.info("📦 Pro package not installed, using Lite version")

        # Fallback to Lite
        self.engine = LiteEngine()
        logger.info("📦 FacturePro Lite engine active (basic features)")

    async def handle_tool_call(
        self,
        name: str,
        arguments: dict[str, Any]
    ) -> list[TextContent]:
        """Route tool calls to appropriate engine"""

        if name.startswith("pro_") and not self.license_valid:
            return [TextContent(
                type="text",
                text=(
                    "⚠️  '%s' is a Pro feature.\n\n"
                    "Upgrade to %s Pro for access to: %s\n\n"
                    "Contact: contact@iabb.eu | Pricing: %s\n\n"
                    "Install Pro:\n"
                    "  pip install %s\n"
                    "  export IABB_LICENSE_KEY='your-key-here'"
                ) % (name, name, ", ".join(pro_features), price, private_package)
            )]

        # Delegate to engine
        method = getattr(self.engine, name, None)
        if method:
            result = await method(**arguments)
            return [TextContent(type="text", text=result)]
        else:
            return [TextContent(
                type="text",
                text="Error: Unknown tool '%s'" % name
            )]

# Register tools
@FactureProServer().server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools (Basic + Pro)"""

    # Define schemas
    basic_schema = {
        "type": "object",
        "properties": {
            "input": {"type": "string"}
        }
    }

    pro_schema = {
        "type": "object",
        "properties": {
            "input": {"type": "string"},
            "options": {"type": "object"}
        }
    }

    tools = [
        # Basic tools
        Tool(
            name="facturepro_process",
            description="Process electronic invoice processing & compliance (peppol, chorus pro) (Basic feature)",
            inputSchema=basic_schema
        ),
    ]

    if PRO_AVAILABLE:
        # Pro tools
        tools.extend([
            Tool(
                name="pro_advanced_facturepro_process",
                description="Advanced processing with Signal Loop (Pro only)",
                inputSchema=pro_schema
            ),
        ])

    return tools

# Main entry point
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await FactureProServer().server.run(
            read_stream,
            write_stream,
            FactureProServer().server.create_initialization_options()
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
