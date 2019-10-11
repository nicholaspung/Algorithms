#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  multiple = {}
  for item in recipe:
    multiple[item] = 0
    try:
      multiple[item] = int(ingredients[item]/recipe[item])
    except KeyError:
      return 0
  
  return min(multiple.values())


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))