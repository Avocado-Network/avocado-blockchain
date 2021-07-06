from typing import Dict

# The rest of the codebase uses slices everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "avocado": 10 ** 12,  # 1 avocado (AVO) is 1,000,000,000,000 slice (1 trillion)
    "slice:": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin slices
}
