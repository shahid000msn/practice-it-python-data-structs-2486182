from collections import deque
class Task(object):
    def __init__(self, taskDesc , hasPriority=False):
        self.taskDesc=taskDesc
        self.hasPriority =hasPriority
    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

task_queue = deque()
def add_task(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_task():
    print("----Printing Queue----")
    for t in task_queue:
        print(t.taskDesc)
    print("********end***********")
    print("")

def main():
    add_task(Task("Make List"))
    print_task()
    add_task(Task("Make a note1", True))
    add_task(Task("Make a note2", False))
    add_task(Task("learn  note1", True))
    print_task()
    #add code here

    return

if __name__ == "__main__":
    main()