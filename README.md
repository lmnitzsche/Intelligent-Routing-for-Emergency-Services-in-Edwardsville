# Intelligent Routing System for Emergency Services in Edwardsville
## CS 456 Final Project - Team Everest

This project aims to create an offline routing system for emergency services (fire departments, police stations, hospitals) in the Edwardsville area. The system uses advanced algorithms to dynamically calculate the fastest route for emergency responders during severe internet outages. The goal is to ensure that emergency responders can reach their destinations as quickly as possible, even without access to real-time GPS data.

## Problem

During severe internet outages, emergency services in Edwardsville cannot rely on GPS technologies, which can severely hinder response times. This project addresses the issue by:

- Creating a comprehensive offline database of mapping data.
- Implementing advanced shortest-path algorithms to ensure optimal route planning for emergency responders.

## Tech Stack

- **Language**: Python
- **Data Source**: Google Maps (for creating offline dataset of distances and times)
- **Algorithms**:
  - **Dijkstra's Algorithm**: For finding the shortest path in a graph with positive edge weights.
  - **Divide and Conquer**: Although this algorithm doesn't have a formal, standard name, it can be classified as a Divide and Conquer-based shortest path algorithm, combining recursive problem solving with a midpoint heuristic and DFS for pathfinding
  - **Bellman-Ford Algorithm**: Handles graphs with negative edge weights, ensuring robustness in dynamic environments.

## Features

### Dataset Creation
Our dataset was built using Google Maps data, focusing on the fastest routes between various emergency services and residential areas in Edwardsville. The dataset includes:

- **Emergency Services**: Fire Departments, Police Stations, Hospitals.
- **Residential Areas**: Key locations including university buildings and student apartment complexes.

We calculated distances in miles and time in minutes to determine the most efficient routes.

### Algorithms
1. **Dijkstra's Algorithm**: Finds the shortest path between nodes based on distance or time.
   - **Time Complexity**: O((V + E) log V)
   - **Space Complexity**: O(V)
2. **Divide and Conquer**: Efficiently breaks down the problem into smaller subproblems, recursively solving for the shortest path.
   - **Time Complexity**: O(E log V)
   - **Space Complexity**: O(log V)
3. **Bellman-Ford**: Works well with graphs containing negative edge weights.
   - **Time Complexity**: O(V * E)
   - **Space Complexity**: O(V)

### Experimentation and Testing
We performed several experiments to evaluate the performance and accuracy of our algorithms:

1. **Efficiency on Original Dataset**: Tested each algorithm on the dataset we created for emergancy services, confirming its efficiency in dense graphs.
2. **Scalability Testing**: Compared the performance of Dijkstra’s, Divide and Conquer, and Bellman-Ford algorithms across different graph sizes.
3. **Varying Conditions**: Simulated dynamic conditions by randomly updating edge weights to simulate traffic congestion and tested algorithm accuracy with sparse matrices.

## Conclusion

This project addresses a critical problem faced by emergency responders in Edwardsville during internet outages, ensuring that they can still access reliable, offline route information. We’re satisfied with the progress made and look forward to future optimizations, such as enhancing the system’s capabilities and integrating it into real-world emergency response workflows.

