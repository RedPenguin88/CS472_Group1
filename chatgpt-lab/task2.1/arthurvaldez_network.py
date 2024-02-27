# Name: Arthur Valdez III
# Date: 11/9/23
# Student ID: 2001802124

import networkx as nx

def add_router(graph, router_name):
# TODO: Add a router to the graph
    validNode = 0
    # Stores the nodes in the graph into a list
    nodeList = list(graph.nodes())
    # Iterates through the list of nodes to find if the node trying to be added already exists.
    for i in range(len(nodeList)):
        if nodeList[i] == router_name:
            validNode = 1
    # If the validNode flag is set to false, then the node doesn't exist yet.
    if validNode == 0:
        graph.add_node(router_name)
    else:
        print("\nThe router name",router_name,"already exists.")
    
def add_connection(graph, router1, router2, cost):
# TODO: Add a connection between two routers
    # Checks if a previous connection was already established.
    if(graph.has_edge(router1,router2)):
        print("\nA connection already exists between",router1,"and",router2,"\nData is being overwritten.")
        graph.remove_edge(router1,router2)
    graph.add_edge(router1,router2, weight=cost)

def ls_algorithm(graph, source_router):
# TODO: Implement the Link-State algorithm using Dijkstra’s algorithm
    nodeList = list(graph.nodes())
    print("\nLS Algorithm ( from source",source_router,")")
    # Iterates through all the nodes and uses each node from the graph as a target node when calling the dijkstra's path function
    for i in range(len(nodeList)):
        # Ensures it doesn't find a path to itself.
        if nodeList[i] != source_router:
            # Checks whether or not the path exists before using the dijkstra functions.
            if(nx.has_path(graph,source_router,nodeList[i])):
                cost = nx.dijkstra_path_length(graph,source_router,nodeList[i])
                dPath = nx.dijkstra_path(graph,source_router,nodeList[i])
                print(source_router,"->",nodeList[i]," Cost: ",cost," Path: ",dPath)
            else:
                print(source_router,"->",nodeList[i],"is not a valid path.")
    
def dv_algorithm(graph, source_router):
# TODO: Implement the Distance-Vector algorithm using Bellman-Fords
    nodeList = list(graph.nodes())
    print("\nDV Algorithm ( from source",source_router,")")
    # Iterates through all the nodes and uses each node from the graph as a target node when calling the bellman ford's path function
    for i in range(len(nodeList)):
        # Ensures it doesn't find a path to itself.
        if nodeList[i] != source_router:
            # Checks whether or not the path exists before using the bellman functions.
            if(nx.has_path(graph,source_router,nodeList[i])):
                cost = nx.bellman_ford_path_length(graph,source_router,nodeList[i])
                dPath = nx.bellman_ford_path(graph,source_router,nodeList[i])
                print(source_router,"->",nodeList[i]," Cost: ",cost," Path: ",dPath)
            else:
                print(source_router,"->",nodeList[i],"is not a valid path.")
            
def main():
# TODO: Initialize a network graph & handle main menu options
    G = nx.Graph()

    # Infinitely loops until a 5 has been entered.
    while True:
        print("\nAssignment 5 - Main Menu")
        print("1. Add Router to Network")
        print("2. Add Cost Connection")
        print("3. Run Link-State Algorithm")
        print("4. Run Distance Vector Algorithm")
        print("5. Exit\n")

        userInp = int(input("Choose an option: "))

        match userInp:
            # Add Router to Network
            case 1:
                routerName = input("\nEnter a router name: ")
                add_router(G,routerName)
            # Add Cost Connection
            case 2:
                if(len(list(G.nodes())) <= 1):
                   print("\nYou need at least two routers to make an edge.")
                else:
                    routerOne = input("\nEnter a router 1: ")
                    routerTwo = input("Enter a router 2: ")
                    cost = int(input("Enter connection cost: "))
                    add_connection(G,routerOne,routerTwo,cost)
            # Run Link-State Algorithm
            case 3:
                if(nx.is_empty(G)):
                    print("\nThere are no edges in this network.")
                else:
                    routerSource = input("\nEnter the source router: ")
                    ls_algorithm(G,routerSource)
            # Run Distance Vector Algorithm
            case 4:
                if(nx.is_empty(G)):
                    print("\nThere are no edges in this network.")
                else:
                    routerSource = input("\nEnter the source router: ")
                    dv_algorithm(G,routerSource)
            # Exit
            case 5:
                exit()
            # Default case
            case _:
                print("Invalid input. Please enter a number from 1-5.\n")
                        

if __name__ == "__main__":
    main()
