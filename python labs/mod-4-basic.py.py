#!/usr/bin/env python
# coding: utf-8

# In[66]:


'''Module 2: Individual Programming Assignment 1
Useful Business Calculations
This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.
    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee
    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos
    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    tax_paid = float(gross_pay*tax_rate)
    Savings = gross_pay-tax_paid-expenses
    return int(Savings)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.
    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.
    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.
    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job
    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    materials_used = num_jobs*job_consumption
    materials_left = total_material - materials_used
    return (str(materials_left)+material_units) 

def interest(principal, rate, periods):
    '''Interest.
    3 points.
    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.
    Round down the final amount.
    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested
    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    investment_value = principal + (principal*(rate*periods))
    return int(investment_value)

def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    final_weight = weight* 0.453592
    height_feet = height[0] * 0.3048
    height_inches = height[1] * 0.0254
    total_height = height_feet + height_inches
    final_bmi = weight/(total_height**2)
    return float(final_bmi)


# In[67]:


savings(200,0.13,50
       )


# In[68]:


material_waste(1000, "lbs", 10, 20)


# In[69]:


interest(1000000,0.2,3)


# In[70]:


body_mass_index(105,[5,10])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




