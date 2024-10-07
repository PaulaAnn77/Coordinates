#  Paula Farebrother
#  Created on 10th August 2024
#  Last updated Oct 2024

# ________________________________________________________________
#              Module: create a graph, run Prim's Algorithm to
#                   create a minimum spanning tree
#                       (MST: W3Schools, 2024)
# ________________________________________________________________

import drawsvg as draw


class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.mst = []

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def add_all_vertexes(self, coords):
        for i in coords:
            self.add_vertex_data(i.x, i)

    def add_all_edges(self, graph_dict):
        for outer_key, inner_dict in graph_dict.items():
            for inner_key, value in inner_dict.items():
                second_vertex = inner_key
                float_value = value

                self.add_edge(outer_key, inner_key, value)

    def prims_algorithm(self):
        in_mst = [False] * self.size
        key_values = [float('inf')] * self.size
        parents = [-1] * self.size

        key_values[0] = 0  # Starting vertex

        for _ in range(self.size):
            u = min((v for v in range(self.size) if not in_mst[v]),
                    key=lambda v: key_values[v])

            in_mst[u] = True

            if parents[u] != -1:  # No print for first vertex since as no parent
                self.mst.append((self.vertex_data[parents[u]], self.vertex_data[
                    u], self.adj_matrix[u][parents[u]]))

            for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u
        return self.mst

    def print_solution(self):
        print("Points and weighted edges in the Minimum Spanning Tree:")
        for element in self.mst:
            print(f"{element[0]} - {element[1]} : {element[2]}")

    def create_svg(self, filename):
        d = draw.Drawing(300, 300, origin=(-15, -15))
        d.set_pixel_scale(7)
        d.set_render_size(2000)

        for u, v, weight_float in self.mst:
            edge = draw.Line(u.x, u.y, v.x, v.y, stroke='blue', stroke_width=2.5,
                             fill='none')
            center_u = (u.x + v.x) / 2
            center_v = (u.y + v.y) / 2
            text = draw.Text(str(weight_float), 1, center_u, center_v,
                             center=0.6, fill='white')

            d.append(edge)
            d.append(text)

        vertexes = set()
        for u, v, weight in self.mst:
            vertexes.add((u.x, u.y))
            vertexes.add((v.x, v.y))

        for i in vertexes:
            d.append(draw.Circle(i[0], i[1], 1.5,
                                 fill='red', stroke_width=0.5, stroke='black'))

        d.save_svg(filename)
        print("svg created successfully.")

# References

# W3schools.com. (2024). W3Schools.com. [online] Available at:
# https://www.w3schools.com/dsa/dsa_algo_mst_prim.php#:~:text=Prim%27s%20algorithm%20finds%20the%20Minimum
# [Accessed 6 August 2024].
