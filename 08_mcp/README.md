## What is MCP 
Stanadizes
1. Transport (stdio for local, HTTP+SSE for remote)
2. Message Format (JSON-RPC 2.0)
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}

```
3. Capability primitives
   1. Tools
   2. Resources
   3. Prompts
4. Discovery, AI can ask MCP server what can you do and get back a machine readable list of tools/resources



## Learning Steps
1. Create basic local MCP
2. Connect to Claude/Claude code and test
3. Create Remote MCP (how to handle auth)
   1. Try huggingface MCP or other third party MCP to understand
4. Connect langgraph




## Python MCP
###
1. Official Python SDK https://github.com/modelcontextprotocol/python-sdk
2. FastMCP https://github.com/prefecthq/fastmcp
3. 
- How to make it public


## JS MCP
- What packages
- How to make it public



## Test
1. MCP inspector



