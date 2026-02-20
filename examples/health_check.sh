#!/bin/bash
# FeedOracle MCP — Quick Health Check
echo "=== Server Health ==="
curl -s https://feedoracle.io/mcp/health | jq .

echo -e "\n=== SSE Connection Test ==="
timeout 3 curl -sN https://feedoracle.io/mcp/sse | head -2

echo -e "\n=== Discovery Endpoint ==="
curl -s https://feedoracle.io/.well-known/mcp/server.json | jq .name,.version,.transports
