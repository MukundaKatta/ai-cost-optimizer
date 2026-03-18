"""CLI for ai-cost-optimizer."""
import sys, json, argparse
from .core import AiCostOptimizer

def main():
    parser = argparse.ArgumentParser(description="Optimize AI infrastructure costs — model selection, batching, caching, routing")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AiCostOptimizer()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"ai-cost-optimizer v0.1.0 — Optimize AI infrastructure costs — model selection, batching, caching, routing")

if __name__ == "__main__":
    main()
