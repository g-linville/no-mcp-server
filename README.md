# No MCP Server

This is a dumb MCP server to connect to the silly [No as a Service](https://github.com/hotheadhacker/no-as-a-service) project.

## Tools

- `say_no`: returns a humorous and creative alternative to the word "no".

## Configuration

Clone the repo somewhere and then run `uv sync` to set up the virtual environment and install the packages.

Then configure your MCP server:

```json
{
  "mcpServers": {
    "no": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/repo",
        "main.py"
      ]
    }
  }
}
```
