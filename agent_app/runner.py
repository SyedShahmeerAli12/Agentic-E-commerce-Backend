# runner.py
from agent_app.agent_core import katalyst_agent

def main():
    """Starts an interactive chat session with the Katalyst agent."""
    print("Katalyst Agent is online. Type 'exit' to end the session.")
    print("-" * 30)

    # The agent's chat method maintains a conversation history automatically
    conversation = katalyst_agent.chat()

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Agent session ended. Goodbye!")
                break

            response = conversation.send(user_input)
            print(f"Katalyst: {response}")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()