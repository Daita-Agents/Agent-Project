"""
Basic test for your agents and workflows.
"""
import pytest
import asyncio

# Example test - replace with your own
@pytest.mark.asyncio
async def test_my_agent():
    """Test the example agent."""
    from agents.my_agent import create_agent

    agent = create_agent()
    result = await agent.process("test data")

    assert result["status"] == "success"
    assert "test data" in result["result"]

@pytest.mark.asyncio
async def test_my_workflow():
    """Test the example workflow."""
    from workflows.my_workflow import create_workflow

    workflow = create_workflow()
    result = await workflow.run("test data")

    assert result["status"] == "success"

if __name__ == "__main__":
    # Run tests directly
    asyncio.run(test_my_agent())
    asyncio.run(test_my_workflow())
    print("✅ All tests passed!")