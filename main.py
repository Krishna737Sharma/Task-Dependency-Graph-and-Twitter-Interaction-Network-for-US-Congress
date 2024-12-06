# 1.	**Construct and Analyse Task Dependency Graph:**

The given problem is related to a directed graph having a task as a node where tasks have dependencies.
a.	Use the “tasks_dependencies.json”  data to construct the graph. The file has details of each task and a list of tasks on which it depends. You need to determine the order in which tasks should be completed. Each task might depend on other tasks, and you need to construct a directed graph based on these dependencies.
b.	Construct a function that finds the order of tasks that must be completed before a given task (X).
c.	Find the strongly connected components present in the graph.
d.	Print all possible topological order.
"""

import json

# Load task dependencies from JSON file
with open('/content/tasks_dependencies.json') as f:
    df= json.load(f)

df

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Construct adjacency matrix
length= len(df)
graph = [[0] * length for _ in range(length)]

for task, dependencies in df.items():
    task_id = int(task.split('_')[1])
    for dependency in dependencies:
        dependency_id = int(dependency.split('_')[1])
        graph[task_id][dependency_id] = 1
        G.add_edge(dependency_id, task_id)

# Print adjacency matrix
print("Adjacency Matrix:")
for row in graph:
    print(row)

#Plot the graph
plt.figure(figsize=(50,50))  # Increase the figure size
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=80, font_size=50, font_color='black', edge_color='blue', arrowsize=10)
plt.show()

# Function to find task order
def task_order(graph, task_x):
    num_tasks = len(graph)
    visited = [False] * num_tasks
    order = []

    def dfs(task):
        visited[task] = True
        for dependency in range(num_tasks):
            if graph[task][dependency] == 1 and not visited[dependency]:
                dfs(dependency)
        order.append(task)

    dfs(task_x)
    return order[::-1]

# Example usage
task_x = 10
print(f"Task Order for Task {task_x}: {task_order(graph, task_x)}")

# Function to find strongly connected components
def stronglyconnected(graph):
    num_tasks = len(graph)
    visited = [False] * num_tasks
    stack = []
    low = [float('inf')] * num_tasks
    disc = [float('inf')] * num_tasks
    sccs = []
    time = 0

    def dfs(task):
        nonlocal time
        visited[task] = True
        low[task] = disc[task] = time
        time += 1
        stack.append(task)

        for neighbor in range(num_tasks):
            if graph[task][neighbor] == 1:
                if not visited[neighbor]:
                    dfs(neighbor)
                    low[task] = min(low[task], low[neighbor])
                elif neighbor in stack:
                    low[task] = min(low[task], disc[neighbor])

        if low[task] == disc[task]:
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                if w == task:
                    break
            sccs.append(scc)

    for task in range(num_tasks):
        if not visited[task]:
            dfs(task)

    return sccs


print("Strongly Connected Components:")
print(stronglyconnected(graph))

# Function to find topological order
def topological_order(graph):
    num_tasks = len(graph)
    visited = [False] * num_tasks
    order = []

    def dfs(task):
        visited[task] = True
        for neighbor in range(num_tasks):
            if graph[task][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
        order.append(task)

    for task in range(num_tasks):
        if not visited[task]:
            dfs(task)

    return order[::-1]


print("Topological Order:")
print(topological_order(graph))

"""# **2.	Twitter Interaction Network for the US Congress:**

This network represents the Twitter interaction network for the 117th United States Congress, both the House of Representatives and Senate. The base data was collected via Twitter’s API; then the empirical transmission probabilities were quantified according to the fraction of times one member retweeted, quoted, tweeted, replied to, or mentioned another member’s tweet.
All the files are given in the “congress_network” folder.Read the readme file for details.

a.	Construct a directed unweighted graph for the given data.

b.	Find strongly connected components.

c.	Print topological order.

"""

import json
import networkx as nx
import matplotlib.pyplot as plt

# Load Twitter interaction network data from JSON file
with open('/content/congress_network_data.json') as f:
    data = json.load(f)

# Extract inList and usernameList
inList = data[0]['inList']
usernameList = data[0]['usernameList']

# Print inList and usernameList
print("inList:", inList)
print("usernameList:", usernameList)

# Create a directed graph
G = nx.DiGraph()

# Construct adjacency matrix
length = len(usernameList)
graph = [[0] * length for _ in range(length)]

for i, node in enumerate(usernameList):
    for j in inList[i]:
        graph[i][j] = 1
        G.add_edge(usernameList[j], node)

# Print adjacency matrix
print("Adjacency Matrix:")
for row in graph:
    print(row)

# Plot the graph
plt.figure(figsize=(50,50))  # Increase the figure size
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=50, font_size=8, font_color='black', edge_color='blue', arrowsize=10)
plt.show()

# Find strongly connected components
print("Strongly Connected Components:")
print(stronglyconnected(graph))

# Print topological order
print("Topological Order:")
print(topological_order(graph))
