from constraint import Problem
from functools import partial
# Step 1: Define Variables and Domains
tasks = [{"task": "report", "start": 1, "end": 15, "order": 1, "needs": ["researcher"], "length": 2}
    , {"task": "Application programming", "start": 5, "end": 25, "order": 2, "needs": ["programmer"], "length": 5},
         {"task": "troubleshooting", "start": 20, "end": 36, "order": 3, "needs": ["tester"], "length": 3}]

tasks1 = ["report", "Application programming", "troubleshooting"]

persons = [{"name": "elliot", "profession": ["tester", "writer"]}, {"name": "jeff", "profession": ["programmer"]}]

time_slots = []
for task in tasks:
    time_slots.append([i for i in range(task.get("start"), (task.get("end") + 1))])

problem = Problem()

for i, task in enumerate(tasks1):
    problem.addVariable(task, time_slots[i])


# Step 2: Define Constraints
def constraint_function(ts1, ts2, ta1, ta2):
    # Example constraint: Tasks cannot be scheduled in the same time slot
    dic1 = {}
    for t in tasks:
        # print(t)
        if t["task"].__eq__(ts1):
            dic1 = t
            break
    dic2 = {}
    for t1 in tasks:
        if t1["task"].__eq__(ts2):
            dic2 = t1
            break

    if dic1["order"] <= dic2["order"]:
        return ta1 + dic1["length"] < ta2
    else:
        return ta1 > ta2 + dic2["length"]


for task1 in tasks1:
    for task2 in tasks1:
        if task1 != task2:
            ts1 = task1
            ts2 = task2
            constraint_with_tasks = partial(constraint_function, ts1, ts2)

            problem.addConstraint(constraint_with_tasks, (task1, task2))

# Step 3: Solve the CSP
solutions = problem.getSolutions()

# Print the solutions
for solution in solutions:
    print(solution)
