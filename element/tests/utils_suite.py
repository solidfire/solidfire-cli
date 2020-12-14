from element.cli import utils
import jsonpickle
import os
import solidfire
import collections

# Check the tree generator:
def test_check_tree_generator():
    """
        SDK1.6 Note:
        Removing this test as print_tree is not supported in 1.6, 
    """
    print("print_tree is not supported in SDK1.6")
    """
    # First, read in the appropriate values:
    # Input:
    resources = os.path.join("element/tests/resources", "FormatterUnitTests")
    with open(os.path.join(resources, "JsonOutput.txt")) as f:
        objectModel=jsonpickle.decode(f.read())

    # Verify that they have all the same lines.
    with open(os.path.join(resources, "TreeDepth3.txt")) as f:
        treeDepth3 = f.read()
    assert collections.Counter(
        utils.get_result_as_tree(objectModel, depth=3).split("\n")
    ) == collections.Counter(
        treeDepth3.split("\n")
    )

    # Verify that if we change the depth, it still has all the same lines.
    with open(os.path.join(resources, "TreeDepth5.txt")) as f:
        treeDepth5 = f.read()
    assert collections.Counter(
        utils.get_result_as_tree(objectModel, depth=5).split("\n")
    ) == collections.Counter(
        treeDepth5.split("\n")
    )
    print("Tree generator is working.")
"""

