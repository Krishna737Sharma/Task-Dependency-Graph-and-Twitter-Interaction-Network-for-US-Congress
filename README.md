# Task Dependency Graph and Twitter Interaction Network for US Congress

## Problem 1: Construct and Analyze Task Dependency Graph

This task involves constructing and analyzing a directed graph representing tasks and their dependencies. Each task is a node in the graph, and the dependencies between tasks are directed edges. The goal is to analyze the task completion order and identify strongly connected components.

### a. Constructing the Graph
- **Input**: The data is provided in the `tasks_dependencies.json` file. This file contains a list of tasks, each with details about its dependencies (other tasks it depends on).
- **Output**: A directed graph representing the tasks and their dependencies.

### b. Finding the Order of Tasks
- **Objective**: Construct a function that determines the order in which tasks should be completed before a given task (X).
- **Explanation**: The function will use topological sorting to find the correct order of tasks, taking into account their dependencies.

### c. Finding Strongly Connected Components (SCC)
- **Objective**: Identify the strongly connected components (SCCs) in the graph.
- **Explanation**: SCCs are subgraphs where every node is reachable from every other node. We will use algorithms like Tarjan’s or Kosaraju’s to find these components.

### d. Printing All Possible Topological Orders
- **Objective**: Print all the possible topological orders for the graph.
- **Explanation**: Topological sorting of a directed graph with dependencies will give the task completion order. Multiple orders can exist for graphs with multiple valid topological sorts.

---

## Problem 2: Twitter Interaction Network for the US Congress

This part of the assignment focuses on the directed unweighted graph representing Twitter interactions among the members of the 117th United States Congress. The interactions were based on empirical data, such as retweets, mentions, replies, etc.

### a. Constructing the Directed Unweighted Graph
- **Input**: Data is provided in the `congress_network` folder.
- **Output**: A directed unweighted graph representing Twitter interactions between members of Congress.

### b. Finding Strongly Connected Components (SCC)
- **Objective**: Identify the strongly connected components (SCCs) in the graph.
- **Explanation**: SCCs are subgraphs where each node is reachable from every other node. We will use algorithms like Tarjan’s or Kosaraju’s to find these components.

### c. Printing the Topological Order
- **Objective**: Print the topological order for the graph.
- **Explanation**: A topological order will show the order of interactions among members in terms of retweets, mentions, etc. This will be computed using topological sorting.

---

## How to Run the Code

1. **Prerequisites**:
   - Install necessary Python packages:
     ```bash
     pip install networkx
     pip install matplotlib
     ```

2. **Input Files**:
   - `tasks_dependencies.json`: Task dependency data for Problem 1.
   - Files in the `congress_network` folder: Data for Problem 2.

3. **Running the Code**:
   - Run the Python scripts for each task (either as a complete module or as separate functions).

4. **Outputs**:
   - The program will output:
     - Task order for Problem 1.
     - Strongly Connected Components (SCCs) for both problems.
     - Topological order for both problems.

---
