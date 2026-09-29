from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

from tools import list_task, add_task, complete_task

tools = [
    list_task,
    add_task,
    complete_task,
]

model = ChatOllama(
    model = 'qwen3:8b',
    temperature=0,
)
model_with_tools = model.bind_tools(tools)

messages = [
    SystemMessage(
        content=(
            "Eres un gestor de tareas"
            "Utiliza las herramientas disponibles para realizar las operaciones solicitadas. No afirmes que has realizado una accion sin utilizar la herramienta correspondiente"
        )
    ),
    HumanMessage(
        content="Añade una tarea llamada 'Estudiar LangGraph'"
    ),
]

respone = model_with_tools.invoke(messages)
print(respone.tool_calls)