# -*- coding: utf-8 -*-
"""백준 4949.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GKueKTReBeAv4wM-NzAuhf5LfSSi9BEy
"""

while True:
  sentence = input()
  if sentence == '.':
    break
  stack = []
  for i in sentence:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(i)
    elif i == ']':
      if len(stack) != 0 and stack[-1] == '[':
        stack.pop()
      else: stack.append(i)
  
  if len(stack) > 0:
    print('no')
  else:
    print('yes')

