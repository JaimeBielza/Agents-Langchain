import json

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_ollama import ChatOllama

from tools import add_task, list_task, complete_task

tools = [
    add_task,
    list_task,
    complete_task,
]

tools_by_name = {
    tool.name: tool for tool in tools
}
model = ChatOllama(
    model='qwen3:8b',
    temperature = 0,
)

model_with_tools = model.bind_tools(tools)

messages = [
    SystemMessage(
        content=("Eres un asistente de tareas. Uitiliza las herramientas para realizar las oepraciones solicitadas. No afirmes que has realiado una acción sin utiliza la herramienta.")
    ),
    HumanMessage(
        content=(
            "Añade la tarea de estududiar cuantica a la lista de tareas"
        )
    ),
]

model_response = model_with_tools.invoke(messages)

messages.append(model_response)

for tool_call in model_response.tool_calls:
    selected_tool = tools_by_name[tool_call["name"]]
    tool_result = selected_tool.invoke(tool_call["args"])

    messages.append(
        ToolMessage(
            content=json.dumps(tool_result, ensure_ascii=False),
            tool_call_id = tool_call["id"],
            name=tool_call["name"],
        )
    )

final_response = model_with_tools.invoke(messages)
print("Respuesta final: ")
print(final_response.content)

print("\nEstado real de las tareas: ")
print(list_task.invoke({}))