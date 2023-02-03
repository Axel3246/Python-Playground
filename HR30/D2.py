"""
Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
"""
import math

mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = mealCost * (tipPercent/100)
tax = mealCost * (taxPercent/100)


totalCost = mealCost + tip + tax
print(round(totalCost))