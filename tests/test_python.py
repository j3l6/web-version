import pytest
from exercises.python_exercise import Product, DigitalProduct

def test_product_discount():
    p = Product("Table", 100)
    assert p.get_discounted_price(0.1) == 90

def test_digital_product_discount_override():
    dp = DigitalProduct("eBook", 50)
    assert dp.get_discounted_price() == 40

@pytest.mark.xfail(reason="Optional: bonus task", strict=False)
def test_digital_product_bonus():
    import inspect
    import ast

    source = inspect.getsource(DigitalProduct)
    tree = ast.parse(source)

    class SuperCallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.found_super_call = False

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id == 'super':
                self.found_super_call = True
            self.generic_visit(node)

    visitor = SuperCallVisitor()
    visitor.visit(tree)

    assert visitor.found_super_call, "DigitalProduct's get_discounted_price method is not implemented correctly."