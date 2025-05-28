import pytest
from lxml import etree
import os
import ast
import inspect
from exercises import xpath_exercise

def test_xml_modification(tmp_path):
    output_file = tmp_path / "output_form.xml"
    xpath_exercise.modify_xml("exercises/input_form.xml", str(output_file))

    tree = etree.parse(str(output_file))
    root = tree.getroot()

    # Check order and position of all elements
    assert root[0].tag == "field" and root[0].attrib["name"] == "author"
    assert root[1].tag == "field" and root[1].attrib["name"] == "name"
    assert root[2].tag == "section" and root[2].text == "Details"
    assert root[3].tag == "button" and root[3].attrib["name"] == "toggle_availability"
    assert root.xpath("//section[text()='Details']")
    assert root.xpath("//button[@name='toggle_availability']")

def test_xpath_targets_correct_element():
    """Ensure the selected XPath targets the correct element."""
    input_tree = etree.parse("exercises/input_form.xml")
    expected_element = input_tree.xpath("//field[@name='author']")[0]

    source = inspect.getsource(xpath_exercise)
    tree = ast.parse(source)

    class XPathExtractor(ast.NodeVisitor):
        def __init__(self):
            self.xpath_expr = None

        def visit_Call(self, node):
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'xpath':
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.xpath_expr = arg.value
            self.generic_visit(node)

    extractor = XPathExtractor()
    extractor.visit(tree)

    if extractor.xpath_expr:
        try:
            actual_element = input_tree.xpath(extractor.xpath_expr)[0]
            assert actual_element == expected_element
        except Exception:
            pytest.fail("XPath expression does not target the correct element or is incorrect.")

@pytest.mark.xfail(reason="Optional: bonus task", strict=False)
def test_xpath_expression_is_correct():
    """Ensure the XPath expression used is correct."""
    source = inspect.getsource(xpath_exercise)
    tree = ast.parse(source)

    class XPathExtractor(ast.NodeVisitor):
        def __init__(self):
            self.xpath_expr = None

        def visit_Call(self, node):
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'xpath':
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.xpath_expr = arg.value
            self.generic_visit(node)

    extractor = XPathExtractor()
    extractor.visit(tree)

    assert extractor.xpath_expr == "//field[@name='author']", \
        f"Incorrect XPath expression used: '{extractor.xpath_expr}'"