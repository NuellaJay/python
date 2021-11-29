
def compress(original):
  results = ""
  last_char = ""
  run_length = 0

  for i in original:
    if i != last_char:
      if last_char:
        results += last_char + str(run_length)
      run_length = 1
      last_char = i 
    else:
      run_length += 1
  results += str(run_length) + last_char 
  return results

print(compress(input()))
