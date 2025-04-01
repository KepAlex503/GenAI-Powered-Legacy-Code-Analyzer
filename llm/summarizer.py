from typing import Dict, List
from llm.openai_client import OpenAIClient


class Summarizer:
    def __init__(self, client: OpenAIClient):
        self.client = client

    def summarize_graph(self, graph_data: Dict[str, List[Dict]]) -> List[Dict[str, str]]:
        """
        Accepts method graph data (dict with nodes and edges),
        sends structured prompts to LLM, and receives business requirement descriptions.
        Returns list of {"method": str, "description": str}
        """
        summaries = []

        # @todo several calls for every node is more precise, but too slow.
        for node in graph_data["nodes"]:
            method_id = node["id"]
            context = self._build_context(node, graph_data["edges"])
            prompt = self._build_prompt(method_id, context)
            response = self.client.get_completion(prompt)
            print(response)
            summaries.append({
                "method": method_id,
                "description": response.strip()
            })

        return summaries

    def _build_context(self, node: Dict, edges: List[Dict]) -> str:
        # Find methods this node calls
        calls = [e["to"] for e in edges if e["from"] == node["id"]]

        # @todo maybe sould also pass where and who use this method ?
        context = f"""
                Method: {node['id']}
                Class: {node.get('class_name')}
                Arguments: {node['args']}
                Return Type: {node.get('return_type')}
                Source File: {node.get('file')}:{node.get('lineno')}
                Calls: {calls}
                """
        return context.strip()

    def _build_prompt(self, method_id: str, context: str) -> str:

        return f"""Given the following Python method context, extract its purpose in one or two sentences. Always add who calls this method.
                
                ### Context ###
                {context}
                
                ### Task ###
                Describe the business functionality or purpose of method `{method_id}`:
                """
