skills = ["Python", "SQL", "Tableau"]

def fav_skill(skill):
  return f"{skill} is our favorite!"


# New function
def add(num_1, num_2):
  return num_1 + num_2



# New function
def sub(num_1, num_2):
  return num_1 - num_2



# New function
def mul(num_1, num_2):
  return num_1 * num_2



def calculate_salary(base_salary, bonus_rate = .1):
  """
    Calculate the total salary based on the base salary and bonus rate

    Args:
        base_salary (float): The base salary.
        bonus_rate (float): The bonus rate. Default is .1.

    Returns:
        total_salary (float): The total salary
  """
  
  tot_salary = base_salary * (1 + bonus_rate)

  return tot_salary




def cal_bonus_rate(total_salary, base_salary):
    """
    Calculates bonus rate based on the total salary and base salary
  
    Args: 
        total_salary (float): The total salary
        Base_salary (float): The base salary
    
    Returns:
        bonus_rate (float): The bonus rate
    """
    bonus_rate = (total_salary - base_salary) / base_salary
    return bonus_rate
