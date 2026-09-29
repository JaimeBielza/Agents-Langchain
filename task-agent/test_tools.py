from tools import add_task, list_task, complete_task


firs_task = add_task.invoke(
    {'title': 'Preparar entrevsita'}
)
second_task = add_task.invoke(
    {
        'title': 'Crear agentes de IA'
    }
)

print(f"Tareas creadas \n1- {firs_task}\n2- {second_task}")


for tarea in list_task.invoke({}):
    print(f'Tarea: {tarea['title']} -- id: {tarea['id']} -- completed: {tarea['completed']}')

print(f'Completando primera tarea:')
print(f'{complete_task.invoke({
    "task_id": 1
})}')

for tarea in list_task.invoke({}):
    print(f'Tarea: {tarea['title']} -- id: {tarea['id']} -- completed: {tarea['completed']}')
