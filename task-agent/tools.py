from langchain_core.tools import tool


tasks: dict[int, dict] = {}
next_task_id = 1

@tool
def add_task(title:str) -> dict:
    """
    Crea una tarea nueva con el titulo indicado.
    """
    global next_task_id
    task = {
        "id": next_task_id,
        "title": title,
        "completed": False
    }
    tasks[next_task_id] = task
    next_task_id += 1
    return task


@tool
def list_task() -> list[dict]:
    """
    Devuelve todas las tareas existentes.
    """
    return list(tasks.values()) 

@tool
def complete_task(task_id: int) -> dict:
    """
    Marca como completa la tarea correspondiente a al task_id
    """

    task = tasks.get(task_id)
    if task is None:
        return {
            "success": False,
            "error": f"No existe ninguna tarea con ID {task_id}"
        }
    else:
        task["completed"] = True
        return {
            "success": True,
            "task": task
        } 
        