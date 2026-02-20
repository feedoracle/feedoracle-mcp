#!/usr/bin/env python3
"""FeedOracle MCP — Python Client Example

Connects via SSE transport, calls compliance_preflight for USDC.
Requires: pip install mcp
"""
import asyncio
from mcp.client.session import ClientSession
from mcp.client.sse import sse_client

SERVER_URL = "https://feedoracle.io/mcp/sse"

async def main():
    async with sse_client(SERVER_URL) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")

            # Run compliance preflight for USDC
            result = await session.call_tool(
                "compliance_preflight",
                arguments={"token": "USDC"}
            )
            print(f"\nUSDC Compliance:\n{result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
