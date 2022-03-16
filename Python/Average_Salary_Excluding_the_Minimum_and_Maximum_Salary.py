# 1491. Average Salary Excluding the Minimum and Maximum Salary

def average(self, salary: List[int]) -> float:
    return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
