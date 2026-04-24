import modules

# Initial list of messages
messages = []

system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

modules.add_user_message(messages, "How to i solve 5x+2=2 for x?")
response = modules.chat(messages, system=system_prompt,temperature=0.5)
print(response)