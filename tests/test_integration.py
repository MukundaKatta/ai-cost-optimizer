"""Integration tests for AiCostOptimizer."""
from src.core import AiCostOptimizer

class TestAiCostOptimizer:
    def setup_method(self):
        self.c = AiCostOptimizer()
    def test_10_ops(self):
        for i in range(10): self.c.process(i=i)
        assert self.c.get_stats()["ops"] == 10
    def test_service_name(self):
        assert self.c.process()["service"] == "ai-cost-optimizer"
    def test_different_inputs(self):
        self.c.process(type="a"); self.c.process(type="b")
        assert self.c.get_stats()["ops"] == 2
    def test_config(self):
        c = AiCostOptimizer(config={"debug": True})
        assert c.config["debug"] is True
    def test_empty_call(self):
        assert self.c.process()["ok"] is True
    def test_large_batch(self):
        for _ in range(100): self.c.process()
        assert self.c.get_stats()["ops"] == 100
