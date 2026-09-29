from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from tools import add_task, complete_task, list_task

tools = [
    add_task,
    complete_task,
    list_task,
]

model = ChatOllama(
    model='qwen3:8b',
    temperature=0,
)

model_with_tools = model.bind_tools(tools)

system_message = SystemMessage(
    content=(
        "Eres un gestor de tareas"
        "Utiliza las herramientas para realizar las operaciones solicitadas"
        "No afirmes que has realizado una acción sin utiliza la herramienta"
    )
)

def call_model(state:MessagesState) -> dict:
    """
    Invoca al modelo utilizando los mensajes almacenados en el estado
    """
    response = model_with_tools.invoke(
        [system_message, *state["messages"]]
    )
    return {
        "messages": [response]

    }

builder = StateGraph(MessagesState)
builder.add_node("agent", call_model)
builder.add_node('tools', ToolNode(tools))

builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    tools_condition,
)

graph = builder.compile()

result = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Añade una tarea llamada 'Preparar cena' completala y listame todas las tareas que tengas almacenadas"
            )
        ]
    }
)

print("Respuesta final: ")
print(f'{result["messages"]}')

print("\nEstado real de las tareas:")
print(list_task.invoke({}))