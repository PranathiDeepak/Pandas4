import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    result_set = set()
    for i in range(len(employee)):
        salary = employee['salary'][i]
        result_set.add(salary)
    df = pd.DataFrame(result_set,columns = ['SecondHighestSalary']).sort_values(by = ['SecondHighestSalary'],ascending=False)
    if len(df)< 2:
        return pd.DataFrame({f'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({f'SecondHighestSalary': df.iloc[1]})