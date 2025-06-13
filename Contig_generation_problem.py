from collections import defaultdict

def parse_input(filename):
    with open(filename, 'r') as f:
        return f.read().strip().split()

def build_de_bruijn_graph(kmers):
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
        out_deg[prefix] += 1
        in_deg[suffix] += 1

    return graph, in_deg, out_deg

def is_1_in_1_out(node, in_deg, out_deg):
    return in_deg[node] == 1 and out_deg[node] == 1

def maximal_non_branching_paths(graph, in_deg, out_deg):
    paths = []
    visited_edges = set()  # Track visited edges as (from,to)

    for node in graph:
        # For all outgoing edges from nodes that are not 1-in-1-out
        if not is_1_in_1_out(node, in_deg, out_deg):
            for neighbor in graph[node]:
                if (node, neighbor) in visited_edges:
                    continue
                path = [node, neighbor]
                visited_edges.add((node, neighbor))
                # Follow path through 1-in-1-out nodes
                while is_1_in_1_out(neighbor, in_deg, out_deg):
                    next_node = graph[neighbor][0]
                    if (neighbor, next_node) in visited_edges:
                        break
                    path.append(next_node)
                    visited_edges.add((neighbor, next_node))
                    neighbor = next_node
                paths.append(path)

    # Now find isolated cycles (1-in-1-out nodes not visited)
    for node in graph:
        if is_1_in_1_out(node, in_deg, out_deg):
            for neighbor in graph[node]:
                if (node, neighbor) in visited_edges:
                    continue
                cycle = [node, neighbor]
                visited_edges.add((node, neighbor))
                current = neighbor
                while current != node:
                    next_node = graph[current][0]
                    if (current, next_node) in visited_edges:
                        break
                    cycle.append(next_node)
                    visited_edges.add((current, next_node))
                    current = next_node
                paths.append(cycle)

    return paths

def path_to_string(path):
    result = path[0]
    for node in path[1:]:
        result += node[-1]
    return result

def main():
    input_file = 'dataset_30189_5.txt'  # Change filename if needed
    output_file = 'output.txt'

    kmers = parse_input(input_file)
    graph, in_deg, out_deg = build_de_bruijn_graph(kmers)
    paths = maximal_non_branching_paths(graph, in_deg, out_deg)
    contigs = [path_to_string(path) for path in paths]

    with open(output_file, 'w') as f:
        for contig in contigs:
            f.write(contig + '\n')

    print("Contigs written to", output_file)

if __name__ == '__main__':
    main()

