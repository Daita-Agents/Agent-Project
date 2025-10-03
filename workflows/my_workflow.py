"""
My Workflow

A simple starter workflow. Replace this with your own logic.
"""
from daita import SubstrateAgent, Workflow

def create_workflow():
    """Create the workflow instance using direct Workflow pattern."""
    workflow = Workflow("My Workflow")

    # Add your agents here
    # agent = SubstrateAgent(name="Agent")
    # workflow.add_agent("agent", agent)

    return workflow

async def run_workflow(data=None):
    """Run the workflow with direct pattern."""
    workflow = create_workflow()

    try:
        await workflow.start()

        # Your workflow logic here
        result = f"Workflow processed: {data}"

        return {
            'status': 'success',
            'result': result
        }

    finally:
        await workflow.stop()

if __name__ == "__main__":
    import asyncio

    async def main():
        result = await run_workflow("Hello, workflow!")
        print(result)

    asyncio.run(main())