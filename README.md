# MCP Catalog - Universal MCP Server Registry

> **Centralized catalog of Model Context Protocol (MCP) servers for AI framework integration**

This repository serves as a **single source of truth** for MCP server configurations across all your AI projects.

## 🎯 Purpose

- **Centralized Management**: One place to maintain MCP server configurations
- **Easy Updates**: Update once, use everywhere
- **Shared Across Projects**: Import this catalog into any project that needs MCP
- **Version Controlled**: Track changes to MCP server configurations

## 📦 What's Inside

- **`mcp_catalog.py`** - Complete registry of all available MCP servers
- **`.env.template`** - Template for configuring tokens/credentials
- **`README.md`** - This documentation

## 🚀 Usage

### As a Git Submodule

```bash
# Add to your project
git submodule add https://github.com/gcolenstra/mcp-catalog.git external/mcp-catalog

# Import in your code
from external.mcp_catalog.mcp_catalog import MCP_CATALOG
```

### As a Python Package

```bash
# Install directly from GitHub
pip install git+https://github.com/gcolenstra/mcp-catalog.git

# Import in your code
from mcp_catalog import MCP_CATALOG
```

### Via URL Download (Simple)

```python
import requests

# Fetch latest catalog
response = requests.get('https://raw.githubusercontent.com/gcolenstra/mcp-catalog/main/mcp_catalog.py')
exec(response.text)  # Now MCP_CATALOG is available
```

## 🔧 Configuration

1. Copy `.env.template` to your project as `.env`
2. Fill in the tokens for services you want to use
3. Only configure what you need - unused services can be left blank

## 📋 Available MCP Servers

See `mcp_catalog.py` for the complete list. Categories include:

- **Development & Version Control**: GitHub, GitLab, Git operations
- **Documentation & Code Intelligence**: Context7, Library docs, Framework guides  
- **AI & Problem Solving**: Sequential thinking, reasoning chains
- **Web & Scraping**: Firecrawl, Puppeteer, web automation
- **Databases**: PostgreSQL, MongoDB, SQLite
- **Cloud Services**: AWS, Azure, cloud integrations
- **File Operations**: Filesystem access, file management
- **And many more...**

## 🔄 Keeping Updated

### If using as submodule:

```bash
cd external/mcp-catalog
git pull origin main
```

### If using as package:

```bash
pip install --upgrade git+https://github.com/gcolenstra/mcp-catalog.git
```

## 🤝 Contributing

Found a new MCP server or need to update configurations?

1. Fork this repository
2. Update `mcp_catalog.py`
3. Submit a Pull Request

## 📄 License

MIT License - Use freely in your projects!

---

**Part of the Lenstra AI Framework** 🚀
