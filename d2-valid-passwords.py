def get_input():
    inp_file = open("d2.txt", "r").readlines()
    inp = {}
    for line in inp_file:
        policy, passwd = line.split(":")
        min, max_and_letter = policy.split("-")
        max, letter = max_and_letter.split()
        inp[passwd.strip()] = (int(min), int(max), letter)
    return inp

def is_passwd_valid(passwd, policy):
  count = 0
  for l in passwd:
    if l == policy[2]:
      count += 1
      if count > policy[1]:
        return False
  if count >= policy[0] and count <= policy[1]:
    return True
  return False

def is_passwd_valid2(passwd, policy):
  if len(passwd) < policy[0] or len(passwd) < policy[1]:
    return False
  if passwd[policy[0]-1] == policy[2]:
    if passwd[policy[1]-1] == policy[2]:
      return False
    else:
      return True
  else:
    if passwd[policy[1]-1] == policy[2]:
      return True
    else:
      return False

def count_val_passwd(inp, validity_func):
  valid_passwd_count = 0
  for passwd, policy in inp.items():
    if validity_func(passwd, policy):
      #  print(policy, passwd)
      valid_passwd_count += 1
  return valid_passwd_count

inpu = get_input()
print(count_val_passwd(inpu, is_passwd_valid))
print(count_val_passwd(inpu, is_passwd_valid2))
