import modules

messages = []

prompt = """Generate 3 different sample AWS CLI commands. each shoud be very short.
"""

modules.add_user_message(messages, prompt)
modules.add_assistant_message(messages, "Here are all three commands in a single block without any comments:\n```bash")

text = modules.chat(messages, stop_sequence=["```"])
text.strip()
print(text)

from IPython.display import Markdown
Markdown(text)