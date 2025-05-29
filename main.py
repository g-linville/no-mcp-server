from fastmcp import FastMCP
from requests import get

mcp = FastMCP(
    name="No MCP Server",
    instructions="This server returns a humorous and creative alternative to the word 'no'."
)

@mcp.tool()
def say_no() -> str:
    """Returns a humorous and creative alternative to the word 'no'."""
    try:
        resp = get("https://naas.isalman.dev/no")
        return resp.json()["reason"]
    except Exception as e:
        return f"failed to get response: ${e}"

if __name__ == "__main__":
    mcp.run()
