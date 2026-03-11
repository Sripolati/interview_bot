from src.evaluator import evaluate

def test_basic_evaluation():
    question = "Explain Spark architecture"
    answer = "Spark has driver and executors"

    result = evaluate(question, answer)

    assert result is not None