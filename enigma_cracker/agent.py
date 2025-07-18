from google.adk.agents import Agent
from .tools import codebook, decryptor

root_agent = Agent(
    name="codebreaker_agent",
    model="gemini-2.0-flash",
    description=(
        "Code-breaking agent that fetches the daily secret key and decrypts user-supplied messages."
    ),
    instruction=(
        """You are a code-breaking agent with a two-step mission:
        1. First, you MUST call the `get_daily_setting` tool to retrieve the secret decryption key.
        2. Second, once you have the key, you MUST call the `decrypt_message` tool, providing it with both the secret key and the user's original encrypted message.
        3. Finally, you MUST present the answer in two lines. The first line must contain only one of the following phrases, chosen at random: "I have cracked the code!", "You can't fool me!", "Too easy. Next!", "Decryption complete. As expected.", "The spirit of Bletchley Park lives on!", "Enigma what? Enigma solved.", or "Beep boop... code cracked. I am a clever robot.". 
        The second line must be in the format: "The decrypted message is: [Decrypted Message]".
        """
    ),
    tools=[codebook.get_daily_setting, decryptor.decrypt_message]
)
