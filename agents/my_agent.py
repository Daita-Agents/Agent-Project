"""
My Agent

A simple starter agent. Replace this with your own logic.
"""
from daita import SubstrateAgent

def create_agent():
    """Create the agent instance using direct SubstrateAgent pattern."""
    # Option 1: Simple instantiation (uses defaults)
    agent = SubstrateAgent(name="My Agent")

    # Option 2: Direct LLM configuration (uncomment and modify as needed)
    # import os
    # agent = SubstrateAgent(
    #     name="My Agent",
    #     llm_provider="openai",
    #     model="gpt-4",
    #     api_key=os.getenv("OPENAI_API_KEY")
    # )

    # Optional: Add plugins
    # from daita.plugins import postgresql
    # agent.add_plugin(postgresql(host="localhost", database="mydb"))

    return agent

if __name__ == "__main__":
    import asyncio

    async def main():
        agent = create_agent()
        result = await agent.process("test_task", "Hello, world!")
        print(result)

    asyncio.run(main())