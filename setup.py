from setuptools import setup, find_packages

setup(
    name="mcp-catalog",
    version="1.0.0",
    description="Universal MCP Server Registry for AI Framework Integration",
    author="Lenstra AI Team",
    author_email="guillaume.coquio@lenstra.fr",
    url="https://github.com/gcolenstra/mcp-catalog",
    py_modules=["mcp_catalog"],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="mcp model-context-protocol ai claude anthropic",
)
