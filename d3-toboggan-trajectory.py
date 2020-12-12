def get_input():
  inp_file = open("d3.txt", "r").readlines()
  inp = []
  for line in inp_file:
    inp.append(line.strip())
  return inp

def is_tree(path, curr_position):
  tree = False
  if path[curr_position] == "#":
    #  print(path, curr_position, "tree")
    tree = True
  else:
    #  print(path, curr_position, "no tree")
    tree = False
  new_position = (curr_position+3) % (len(path))
  return (tree, new_position)

def get_tree_count(inp):
  tree_count = 0
  curr_position = 3
  for i in range(1, len(inp)):
    tree, curr_position = is_tree(inp[i], curr_position)
    if tree:
      tree_count += 1
  return tree_count

def is_tree2(path, curr_position, horiz_move):
  tree = False
  if path[curr_position] == "#":
    #  print(path, curr_position, "tree")
    tree = True
  else:
    #  print(path, curr_position, "no tree")
    tree = False
  new_position = (curr_position + horiz_move) % (len(path))
  return (tree, new_position)

def get_tree_count2(inp, slope):
  horiz_move, vert_move = slope
  tree_count = 0
  curr_position = horiz_move
  for i in range(vert_move, len(inp), vert_move):
    tree, curr_position = is_tree2(inp[i], curr_position, horiz_move)
    if tree:
      tree_count += 1
  return tree_count

print(get_tree_count(get_input()))
trees1 = get_tree_count2(get_input(), (1,1))
trees2 = get_tree_count2(get_input(), (3,1))
trees3 = get_tree_count2(get_input(), (5,1))
trees4 = get_tree_count2(get_input(), (7,1))
trees5 = get_tree_count2(get_input(), (1,2))
print(trees1, trees2, trees3, trees4, trees5)
print(trees1 * trees2 * trees3 * trees4 * trees5)

