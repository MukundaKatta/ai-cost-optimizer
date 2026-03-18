"""Tests for CostOptimizer."""
import pytest
from src.costoptimizer import CostOptimizer

def test_init():
    obj = CostOptimizer()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = CostOptimizer()
    result = obj.collect_usage(input="test")
    assert result["processed"] is True
    assert result["operation"] == "collect_usage"

def test_multiple_ops():
    obj = CostOptimizer()
    for m in ['collect_usage', 'analyze_costs', 'recommend_model_switch']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = CostOptimizer()
    r1 = obj.collect_usage(key="same")
    r2 = obj.collect_usage(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = CostOptimizer()
    obj.collect_usage()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = CostOptimizer()
    obj.collect_usage(x=1)
    obj.analyze_costs(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
