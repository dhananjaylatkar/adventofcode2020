def get_input():
  inp_file = open("d1.txt", "r").readlines()
  inp = []
  for line in inp_file:
    inp.append(int(line))
  return inp

def sum_mul2(inp):
  diffs = set()
  for val in inp:
    if 2020-val in diffs:
      return val*(2020-val)
    else:
      diffs.add(val)
  return -1

def sum_mul3(inp):
  diffs = set()
  entries = len(inp)
  for i in range(entries):
    for j in range(i+1, entries):
      for k in range(j+1, entries):
        if inp[i]+inp[j]+inp[k] == 2020:
          return inp[i]*inp[j]*inp[k]
  return -1

def sum_mul3better(inp):
  sums = {}
  entries = len(inp)
  for i in range(entries):
    for j in range(i+1, entries):
      sums[inp[i]+inp[j]] = (i,j)
  for val in inp:
    if 2020-val in sums.keys():
      return val*inp[sums[2020-val][0]]*inp[sums[2020-val][1]]
  return -1

inpu = get_input()
print(sum_mul2(inpu))
print(sum_mul3(inpu))
print(sum_mul3better(inpu))
