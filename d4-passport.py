import re

def get_input():
  inp_file = open("d4.txt", "r").readlines()
  inp = []
  fields = {}
  for line in inp_file:
    if line == "\n":
      inp.append(fields)
      fields = {}
    for item in line.split():
      fields[item.split(":")[0]] = item.split(":")[1]
  return inp

def valid_passports(inp):
  valid_passports_count = len(inp)
  expected_fields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  for passport in inp:
    for field in expected_fields:
      if field not in passport.keys():
        valid_passports_count -= 1
        break
  return valid_passports_count

def validate_field_val(field, val):
  if field in ["byr", "iyr", "eyr"]:
    val = int(val)
  else:
    val = str(val)

  if field == "byr":
    if val >= 1920 and val <= 2002:
      return True
    return False

  if field == "iyr":
    if val >= 2010 and val <= 2020:
      return True
    return False

  if field == "eyr":
    if val >= 2020 and val <= 2030:
      return True
    return False

  if field == "hgt":
    try:
      height = int(re.search(r'\d+', val).group())
      unit = str(re.search(r'\D+', val).group())
    except:
      return False
    if unit == "cm":
      if height >= 150 and height <= 193:
        return True
    if unit == "in":
      if height >= 59 and height <= 76:
        return True
    return False

  if field == "hcl":
    try:
      re.search(r'^#([a-f0-9]{6})$', val).group()
      return True
    except:
      return False

  if field == "ecl":
    if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
      return True
    return False

  if field == "pid":
    try:
      re.search(r'^([0-9]{9})$', val).group()
      return True
    except:
      return False

def valid_passports2(inp):
  valid_passports_count = len(inp)
  expected_fields = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  for passport in inp:
    for field in expected_fields:
      if field not in passport.keys():
        valid_passports_count -= 1
        break
      else:
        if not validate_field_val(field, passport[field]):
          valid_passports_count -= 1
          break
  return valid_passports_count

# color - ^#([a-f0-9]{6})$
# 9digits - ^([0-9]{9})$

inpu = get_input()
print(valid_passports(inpu))
print(valid_passports2(inpu))
