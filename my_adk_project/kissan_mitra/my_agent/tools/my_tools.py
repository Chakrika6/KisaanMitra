from google.adk import Agent

# Tool function
def getUserInfo(name: str) -> str:
    """
    Get user information from the database by name.

    Args:
        name: The name of the user to get information about.

    Returns:
        A string containing the user information.
    """
    return f"User {name} is a Computer Science student at MS Ramaiah Institute of Technology."

# Define the root agent
prompt = """
You are a helpful customer service assistant. 
You can retrieve information about users based on their names using the provided tool.
"""

root_agent = Agent(
    name="customer_service_agent",
    model="gemini-2.5-pro",
    instruction=prompt,
    tools=[getUserInfo],
    description="A customer service agent that can handle all customer service requests.",
)
