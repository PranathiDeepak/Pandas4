import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result_set = set()
    for i in range(len(employee)):
        salary = employee['salary'][i]
        result_set.add(salary)
    df = pd.DataFrame(result_set,columns = ['getNthHighestSalary']).sort_values(by = ['getNthHighestSalary'],ascending=False)
    if N>len(df) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': df.iloc[N-1]})