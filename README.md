# Test Project — Agent Examples

A small multi-agent example project with three example agents.

Purpose
- Provide a minimal structure for experimenting with simple Python agents.

Repository layout

- `my-first-agent/` — minimal example agent
- `tarvel_planner_agent/` — travel planner agent (note: directory name preserved)
- `tool_agent/` — tool-using agent
- `requirements.txt` — Python dependencies

Quick start (Windows PowerShell)

1. Create and activate a virtual environment

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Copy environment file and edit values

```powershell
copy .env.example .env
# then open .env in your editor and put real values
```

4. Run an agent (example)

```powershell
# run a simple module if present, e.g.:
python -m my-first-agent.agent
```
