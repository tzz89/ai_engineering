from fastmcp import FastMCP

mcp = FastMCP(name="Calculator")


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


@mcp.tool(name="add", description="Adds two numbers.", tags=["math", "arithmetic"])
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers."""
    return a - b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    mcp.run()
