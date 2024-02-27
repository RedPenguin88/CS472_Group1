# Name: Arthur Valdez III
# Date: 11/9/23
# Student ID: 2001802124

import networkx as nx

def add_router(graph, router_name):
    # TODO: Add a router to the graph
    if router_name not in graph.nodes():
        graph.add_node(router_name)
    else:
        print("\nThe router name", router_name, "already exists.")

def add_connection(graph, router1, router2, cost):
    # TODO: Add a connection between two routers
    if graph.has_edge(router1, router2):
        print("\nA connection already exists between", router1, "and", router2, "\nData is being overwritten.")
        graph.remove_edge(router1, router2)
    graph.add_edge(router1, router2, weight=cost)

def ls_algorithm(graph, source_router):
    # TODO: Implement the Link-State algorithm using Dijkstra’s algorithm
    nodeList = list(graph.nodes())
    print("\nLS Algorithm ( from source", source_router, ")")
    for target_router in nodeList:
        if target_router != source_router and nx.has_path(graph, source_router, target_router):
            cost = nx.dijkstra_path_length(graph, source_router, target_router)
            dPath = nx.dijkstra_path(graph, source_router, target_router)
            print(source_router, "->", target_router, " Cost: ", cost, " Path: ", dPath)
        else:
            print(source_router, "->", target_router, "is not a valid path.")

def dv_algorithm(graph, source_router):
    # TODO: Implement the Distance-Vector algorithm using Bellman-Fords
    nodeList = list(graph.nodes())
    print("\nDV Algorithm ( from source", source_router, ")")
    for target_router in nodeList:
        if target_router != source_router and nx.has_path(graph, source_router, target_router):
            cost = nx.bellman_ford_path_length(graph, source_router, target_router)
            dPath = nx.bellman_ford_path(graph, source_router, target_router)
            print(source_router, "->", target_router, " Cost: ", cost, " Path: ", dPath)
        else:
            print(source_router, "->", target_router, "is not a valid path.")

def main():
    # TODO: Initialize a network graph & handle main menu options
    G = nx.Graph()

    while True:
        print("\nAssignment 5 - Main Menu")
        print("1. Add Router to Network")
        print("2. Add Cost Connection")
        print("3. Run Link-State Algorithm")
        print("4. Run Distance Vector Algorithm")
        print("5. Exit\n")

        user_inp = int(input("Choose an option: "))

        if user_inp == 1:
            router_name = input("\nEnter a router name: ")
            add_router(G, router_name)
        elif user_inp == 2:
            if len(list(G.nodes())) <= 1:
                print("\nYou need at least two routers to make an edge.")
            else:
                router_one = input("\nEnter a router 1: ")
                router_two = input("Enter a router 2: ")
                cost = int(input("Enter connection cost: "))
                add_connection(G, router_one, router_two, cost)
        elif user_inp == 3:
            if nx.is_empty(G):
                print("\nThere are no edges in this network.")
            else:
                router_source = input("\nEnter the source router: ")
                ls_algorithm(G, router_source)
        elif user_inp == 4:
            if nx.is_empty(G):
                print("\nThere are no edges in this network.")
            else:
                router_source = input("\nEnter the source router: ")
                dv_algorithm(G, router_source)
        elif user_inp == 5:
            exit()
        else:
            print("Invalid input. Please enter a number from 1-5.\n")

if __name__ == "__main__":
    main()
