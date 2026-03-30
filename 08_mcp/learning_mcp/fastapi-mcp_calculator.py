# Create FastAPI server with http endpoint
# convert to mcp server

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


app = FastAPI(
    title="MCP Calculator API",
    description="API for calculating MCP values",
    version="1.0.0",
)


@app.post(
    "/multiply",
    summary="Multiply two numbers",
    description="Returns the product of two numbers",
)
def multiply(a: float, b: float):
    return {"result": a * b}


@app.post(
    "/add", summary="Add two numbers", description="Returns the sum of two numbers"
)
def add(a: float, b: float):
    return {"result": a + b}


@app.post(
    "/subtract",
    summary="Subtract two numbers",
    description="Returns the difference of two numbers",
)
def subtract(a: float, b: float):
    return {"result": a - b}


@app.post(
    "/divide",
    summary="Divide two numbers",
    description="Returns the quotient of two numbers",
)
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}


# Convert FastAPI app to MCP server
mcp = FastApiMCP(app, name="MCP Calculator")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8002)
