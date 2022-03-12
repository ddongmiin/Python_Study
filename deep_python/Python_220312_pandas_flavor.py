import pandas as pd
import numpy as np
import pandas_flavor as pf
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 코로나 데이터
data_raw = pd.read_csv("https://raw.githubusercontent.com/GiblesDeepMind"
                       "/deepPythonAnalysis/master/interpretation/covid19_korea.csv"
                       , encoding='cp949', parse_dates=['일자'])
data_raw = data_raw.set_index('일자')

print(data_raw.head())

# 판다스 객체 타입 비교해보기
print(type(data_raw.groupby(['일자'])['계(명)']))
print(type(data_raw.groupby(['일자'])['계(명)'].mean()))
print(type(data_raw.groupby(['일자'])['계(명)'].mean().reset_index()))
print(type(data_raw.groupby(['일자'])['계(명)'].mean().reset_index().head()))

"""
pandas_flavor로 pandas api확장하기
---------------------------------

1. 지정한 일자로부터 n일 후 집계 값 구하기
"""


@pf.register_dataframe_method
def idx_after_nday(df: pd.DataFrame, start_date: str, nday: int):
    """시작일로부터 nday 이후 값을 인덱싱합니다."""
    end_date = datetime.strptime(start_date, '%Y-%m-%d') + relativedelta(days=nday)
    return df.loc[start_date:end_date]


data_raw.idx_after_nday('2020-02-01', 10)
data_raw.idx_after_nday('2020-02-01', 10)['계(명)'].sum()


# 샘플 함수
def sample1(a:int):
    def sample2(b:int):
        return a + b
    return sample2


sample1(3)(3)





