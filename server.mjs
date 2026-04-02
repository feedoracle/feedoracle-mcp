import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import express from "express";

const REMOTE_URL = process.env.FEEDORACLE_URL || "https://feedoracle.io/mcp/";

const app = express();
app.use(express.json());

// Health endpoint
app.get("/health", (req, res) => {
  res.json({ status: "healthy", remote: REMOTE_URL, proxy: true });
});

// Forward all MCP requests to the remote FeedOracle server
app.all("/mcp", async (req, res) => {
  try {
    const response = await fetch(REMOTE_URL, {
      method: req.method,
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
      },
      body: req.method !== "GET" ? JSON.stringify(req.body) : undefined,
    });
    
    const contentType = response.headers.get("content-type") || "application/json";
    res.set("Content-Type", contentType);
    res.status(response.status);
    
    const text = await response.text();
    res.send(text);
  } catch (err) {
    res.status(502).json({ error: "upstream_error", message: err.message });
  }
});

app.all("/mcp/*", async (req, res) => {
  try {
    const subpath = req.path.replace("/mcp", "");
    const response = await fetch(REMOTE_URL + subpath, {
      method: req.method,
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
      },
      body: req.method !== "GET" ? JSON.stringify(req.body) : undefined,
    });
    
    const contentType = response.headers.get("content-type") || "application/json";
    res.set("Content-Type", contentType);
    res.status(response.status);
    
    const text = await response.text();
    res.send(text);
  } catch (err) {
    res.status(502).json({ error: "upstream_error", message: err.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`FeedOracle MCP Proxy listening on port ${PORT}`);
  console.log(`Forwarding to: ${REMOTE_URL}`);
});
