from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo")   # temperature=0.1

"""
if __name__ == '__main__':
    message = HumanMessage(content="Hello, can you answer my question? yes or no?")
    message = HumanMessage(content="Do you have a connection to a network?")
    response = model.invoke([message])
    print(response.content)
"""

if __name__ == '__main__':
    messages = [
        HumanMessage(content="Hello, my name is Baris and my surname is Polat. Can you help me please?"),
        AIMessage(content="Hello Baris, how can i help you?"),
        HumanMessage(content="What is my surname?"),
        ]
    response = model.invoke(messages)
    print(response.content)