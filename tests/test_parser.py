import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.trend_parser import generate_outfit

def test_generate_outfit():
    trend = "coastal grandmother"
    output = generate_outfit(trend)
    assert isinstance(output, str)
    assert len(output) > 30  # Minimum length
    assert "shirt" in output.lower() or "top" in output.lower()

if __name__ == "__main__":
    test_generate_outfit()
    print("✅ Trend parser test passed")