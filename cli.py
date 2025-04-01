import argparse
from pathlib import Path
import matplotlib.pyplot as plt
from analyzer.ast_parser import analyze_directory
from analyzer.graph_builder import GraphBuilder
from llm.openai_client import OpenAIClient
from llm.summarizer import Summarizer
from report.generator import ReportGenerator
import networkx as nx

# @should be from env vars from the box
from dotenv import load_dotenv
load_dotenv()

# @todo docker build more conviniant ?



def main():
    parser = argparse.ArgumentParser(
        description="Code Analyzer – Extract business requirements from Python codebases"
    )
    parser.add_argument(
        "--repo-path", "-r", type=Path, required=True, help="Path to the Python codebase directory"
    )
    parser.add_argument(
        "--output", "-o", type=Path, required=True, help="Path to the output markdown report"
    )
    args = parser.parse_args()

    print(f"Analyzing code at: {args.repo_path}")
    method_data = analyze_directory(args.repo_path)

    print("Building invocation graph...")
    graph = GraphBuilder()
    nx_graph = graph.build_graph(method_data)
    graph_data = graph.export_as_dict()
    # print(graph_data)
    # plt.figure(figsize=(12, 8))
    # pos = nx.spring_layout(nx_graph, seed=42)
    # nx.draw(
    #     nx_graph,
    #     pos,
    #     with_labels=True,
    #     node_color="skyblue",
    #     node_size=2500,
    #     font_size=10,
    #     font_weight="bold",
    #     edge_color="gray",
    #     arrows=True,
    # )
    # plt.title("Method Invocation Graph", fontsize=14)
    # plt.tight_layout()
    # plt.show()

    print("Summarizing business logic using LLM...")
    llm_client = OpenAIClient()
    summarizer = Summarizer(llm_client)

    # Attach file/lineno info for reporting
    method_lookup = {m['name'] if not m['class_name'] else f"{m['class_name']}.{m['name']}": m for m in method_data}
    summaries = summarizer.summarize_graph(graph_data)
    for s in summaries:
        method = method_lookup.get(s["method"])
        if method:
            s["file"] = method["file"]
            s["lineno"] = method["lineno"]

    print(f"Generating report at: {args.output}")
    report = ReportGenerator(args.output)
    report.generate_markdown(summaries)

    print("Done! Report generated.")


if __name__ == "__main__":
    main()
