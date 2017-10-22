import doctest


def if_list_in_list(base_string, sub_string):
  """
  >>> if_list_in_list([1,2,3, 1,3,7, 8,9,0],[1,3,7])
  True
  >>> if_list_in_list([1,2,3,4,5], [5,4,3])
  False
  >>> if_list_in_list([1,2,3,4], [1,2])
  True
  """
  strike = 0
  for pos in range(len(base_string)):
    for idx, base_string_element in enumerate(base_string[pos:pos+len(sub_string)]):
      if base_string_element == sub_string[idx]:
        strike += 1
      elif strike == len(sub_string):
        return True
      else:
        strike = 0
        break
  
  return False


if __name__ == '__main__':
  doctest.testmod()
