# Daita-Agents

A Daita AI agent project.

## Quick Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your LLM API key:
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

## Free Local Development

Build and test your agents locally - completely free:

```bash
# Test the example agent
python agents/my_agent.py

# Test all components
daita test

# Watch for changes while developing
daita test --watch

# Create new components
daita create agent my_new_agent
daita create workflow my_new_workflow
```

## Production Cloud Hosting

Ready to deploy to the cloud? Get 24/7 hosting, monitoring, and insights:

```bash
# Get your API key at daita-tech.io
export DAITA_API_KEY='your-key-here'

# Deploy to cloud
daita push                   # Deploy to production

# Monitor your deployments
daita status                 # Deployment status
daita logs                   # View execution logs
```

## Project Structure

```
Daita-Agents/
├── agents/          # Your AI agents (free to create & test)
│   └── my_agent.py
├── workflows/       # Your workflows (free to create & test)
│   └── my_workflow.py
├── data/           # Data files
├── tests/          # Tests
└── daita-project.yaml  # Project config
```

## Command Reference

**Free Commands (Local Development):**
- `daita test` - Test all agents and workflows
- `daita test --watch` - Development mode with auto-reload
- `daita create agent <name>` - Create new agent
- `daita create workflow <name>` - Create new workflow

**Premium Commands (Cloud Hosting):**
- `daita push <env>` - Deploy to cloud
- `daita status` - Monitor deployments
- `daita logs <env>` - View execution logs
- `daita run <agent>` - Execute remotely

## Learn More

- 🚀 [Get API Key](https://daita-tech.io) - Start your free trial
- 📚 [Documentation](https://docs.daita-tech.io)