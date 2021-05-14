todo = []
todo_2 = []

while True:
    action = input('Choose the action: A) Add the task, B) Show the task')
    if action == "A":
        todo = input("Task")
        deadline = input('Deadline')
        time_added = input('Time added')
        todo_2.append([todo, deadline, time_added])

    elif action == "B":
        for i in todo_2:
            print(i[0], i[1], i[2])

    else: print('Choose the right action the one which you choose is not valid!')


