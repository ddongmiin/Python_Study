"""
Python Dot의 의미에 대해서 알아봅니다.
"""

import pandas as pd

test_data = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=['A', 'B', 'C'])
test_data.info()