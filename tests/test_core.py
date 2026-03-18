"""Tests for AiCostOptimizer."""
from src.core import AiCostOptimizer
def test_init(): assert AiCostOptimizer().get_stats()["ops"] == 0
def test_op(): c = AiCostOptimizer(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AiCostOptimizer(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AiCostOptimizer(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AiCostOptimizer(); r = c.process(); assert r["service"] == "ai-cost-optimizer"
