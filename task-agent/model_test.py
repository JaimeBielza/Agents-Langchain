from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

model = ChatOllama(
    model='qwen3:8b',
    temperature=0
)

messages = [
    SystemMessage(
        content='Eres un asistente conciso, Responde siempre en español'
    ),
    HumanMessage(
        content='Explica en una frase que diferencia a un LLM de un agente'
    )
]

response = model.invoke(messages)
print(response.content)