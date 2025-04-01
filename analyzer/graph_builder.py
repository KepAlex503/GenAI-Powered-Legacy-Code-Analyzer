import networkx as nx
from typing import List, Dict, Any


class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()

    def build_graph(self, methods: List[Dict[str, Any]]) -> nx.DiGraph:
        """
        Build a directed graph where:
        - Each node is a method (fully qualified)
        - Each edge represents a method call from one to another
        """
        method_lookup = {
            self._get_full_name(method): method
            for method in methods
        }

        # Add all methods as nodes with metadata
        for full_name, method in method_lookup.items():
            self.graph.add_node(full_name, **{
                "args": method["args"],
                "return_type": method["return_type"],
                "file": method["file"],
                "lineno": method["lineno"],
                "class_name": method["class_name"]
            })

        # Add edges for method calls
        for method in methods:
            caller = self._get_full_name(method)
            for callee_name in method["calls"]:
                for potential_target in method_lookup.keys():
                    if potential_target.endswith(f".{callee_name}") or potential_target == callee_name:
                        self.graph.add_edge(caller, potential_target)
                        break

        return self.graph

    @staticmethod
    def _get_full_name(method: Dict[str, Any]) -> str:
        return f'{method["class_name"]}.{method["name"]}' if method["class_name"] else method["name"]

    def export_as_dict(self) -> Dict[str, Any]:
        """export the graph as a dict for serialization or LLM input"""
        return {
            "nodes": [
                {"id": node, **self.graph.nodes[node]}
                for node in self.graph.nodes
            ],
            "edges": [
                {"from": src, "to": dst}
                for src, dst in self.graph.edges
            ]
        }
