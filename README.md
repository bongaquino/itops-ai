# itops-ai — IT Ops + AI Engineering Journey

# itops-ai 🤖
> IT Ops + AI Engineering Journey | Built with Claude API + MCP

## About
This repository documents the evolution of an IT Generalist into an AI Engineer.
Every real IT problem solved here becomes an automation artifact — documented,
versioned, and reusable. Built with Claude API, Claude Code, and a full MCP stack.

## Structure

```
itops-ai/
├── python/
│   ├── core/
│   │   └── claude_client.py     ← Claude API wrapper
│   ├── agents/                  ← Domain-specific AI agents
│   ├── utils/
│   │   ├── config.py            ← Env/config loader
│   │   └── logger.py            ← Consistent logging
│   └── requirements.txt
├── kubernetes/                  ← K8s automation, AKS, troubleshooting
├── secupi/                      ← SecuPI components, policies, integrations
├── cloud-computing/             ← Azure, AWS, GCP configs and IaC
├── data-warehouses-lakes/       ← Snowflake, S3, Delta Lake, pipelines
├── databases/                   ← PostgreSQL, MySQL, MongoDB, Redis
├── sql-clients/                 ← Query libraries, DBeaver configs
├── java/                        ← Java configs, AI-assisted scripts
├── docs/                        ← Architecture diagrams, runbooks
└── archive/                     ← Completed experiments, preserved
```

## Quick Start
```bash
# Clone
cd ~/Documents/Local_Repo/itops-ai

# Set up Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic

# Configure
vi .env
# add: ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE

# Test connection
python python/core/claude_client.py
```

## Core Pattern
Every automation in this repo follows the same pattern:
```python
from core.claude_client import ClaudeClient

client = ClaudeClient()
response = client.ask(
    prompt="Your IT problem here",
    system="You are an expert in [domain].",
    verbose=True
)
print(response)
```

## Tech Stack
- **AI Engine**: Claude API (claude-sonnet-4-6) via Anthropic Python SDK
- **Agentic Tools**: Claude Code + MCP stack (GitHub, Playwright, Sequential Thinking, Memory, Chrome DevTools, SecuPI)
- **Infra**: Kubernetes (AKS), Azure, AWS
- **Data**: Snowflake, PostgreSQL, MongoDB, Redis, S3, Delta Lake
- **Languages**: Python, SQL, Java, Bash

## Domains & Status

| Domain | Path | Status |
|--------|------|--------|
| Kubernetes / AKS | `kubernetes/` | 🔜 next |
| SecuPI | `secupi/` | 🔜 planned |
| Cloud (Azure/AWS) | `cloud-computing/` | 🔜 planned |
| Snowflake / Data Lakes | `data-warehouses-lakes/` | 🔜 planned |
| Databases | `databases/` | 🔜 planned |
| SQL Clients | `sql-clients/` | 🔜 planned |
| Java | `java/` | 🔜 planned |

## Philosophy
> Every IT problem solved manually is an automation opportunity.
> Every automation is an AI engineering artifact.
> Every artifact gets documented and archived here.

## Author
IT Generalist → AI Engineer
Built with Claude AI + MCP agentic stack
