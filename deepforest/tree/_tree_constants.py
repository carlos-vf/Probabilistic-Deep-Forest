# Initialize constants with placeholders
DTYPE = None
DOUBLE = None
CRITERIA_CLF = {}
CRITERIA_REG = {}
DENSE_SPLITTERS = {}

try:
    # Import Cython modules only if they can be loaded
    from . import _tree
    from . import _splitter
    from . import _criterion

    # Assign the actual values from the loaded Cython modules
    DTYPE = _tree.DTYPE
    DOUBLE = _tree.DOUBLE

    CRITERIA_CLF = {"gini": _criterion.Gini, "entropy": _criterion.Entropy}
    CRITERIA_REG = {"mse": _criterion.MSE, "mae": _criterion.MAE}

    DENSE_SPLITTERS = {
        "best": _splitter.BestSplitter,
        "random": _splitter.RandomSplitter,
    }
except ImportError:
    pass