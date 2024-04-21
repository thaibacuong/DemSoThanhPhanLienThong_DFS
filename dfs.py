import networkx as nx
import matplotlib.pyplot as plt

def DFS(graph):
    count = 0
    time = 0
    color = {vertex: 'white' for vertex in graph}
    father = {vertex: None for vertex in graph}
    d = {vertex: 0 for vertex in graph}
    f = {vertex: 0 for vertex in graph}
    components = []

    def DFSVisit(vertex):
        nonlocal time
        nonlocal count
        color[vertex] = 'gray'
        time += 1
        d[vertex] = time
        components[-1].append(vertex)  # Thêm đỉnh vào thành phần liên thông hiện tại
        for neighbor in graph[vertex]:
            if color[neighbor] == 'white':
                father[neighbor] = vertex
                DFSVisit(neighbor)
            elif color[neighbor] == 'gray':
                return True
        color[vertex] = 'black'
        time += 1
        f[vertex] = time
        return False

    for vertex in graph:
        if color[vertex] == 'white':
            count += 1
            components.append([])  # Bắt đầu một thành phần liên thông mới
            DFSVisit(vertex)

    # Loại bỏ các thành phần liên thông không chứa đỉnh nào
    components = [component for component in components if len(component) > 1]  # Chỉ giữ lại các thành phần có nhiều hơn một đỉnh

    return count, components

def build_graph():
    num_vertices = int(input("Nhập số đỉnh của đồ thị: "))
    graph = {str(i): [] for i in range(num_vertices)}

    print("Nhập cạnh của đồ thị (nhập 'done' để kết thúc):")
    while True:
        edge = input("Nhập cạnh (theo định dạng: đỉnh1 đỉnh2): ").split()
        if edge[0] == 'done':
            break
        if len(edge) != 2:
            print("Định dạng cạnh không hợp lệ. Vui lòng nhập lại.")
            continue
        u, v = edge
        if u.isdigit() and v.isdigit():
            u, v = int(u), int(v)
            if 0 <= u < num_vertices and 0 <= v < num_vertices:
                graph[str(u)].append(str(v))
                graph[str(v)].append(str(u))  # Thêm cạnh vô hướng
            else:
                print("Đỉnh không hợp lệ. Vui lòng nhập lại.")
        else:
            print("Đỉnh phải là số nguyên không âm. Vui lòng nhập lại.")

    return graph

def draw_graph(graph):
    G = nx.Graph()
    for vertex in graph:
        for neighbor in graph[vertex]:
            G.add_edge(vertex, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800)
    plt.show()

# Xây dựng đồ thị từ dữ liệu nhập từ bàn phím
G = build_graph()

# Thực hiện DFS và đếm số thành phần liên thông
component_count, components = DFS(G)

# In ra số thành phần liên thông trong đồ thị
print("Số thành phần liên thông trong đồ thị là:", len(components))

# In ra các đỉnh trong từng thành phần liên thông
for i, component in enumerate(components, 1):
    print(f"Thành phần liên thông {i}: {component}")

# Vẽ đồ thị
draw_graph(G)
