class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    self.name = None
    print(f"Object instance created. value: '{self.value}'")

  def __repr__(self):
    return f"<Node object '{self.name}'>"

  def get_value(self):
    return self.value

  def set_link_node(self, link_node):
    self.link_node = link_node
  
  def get_link_node(self):
    return self.link_node


# Test case 1
print("\n---- Test case 1 ----\n")

yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# add name attribute to the object
yacko.name = 'yacko'
wacko.name = 'wacko'
dot.name = 'dot'

print("")
print(yacko)
print(wacko)
print(dot, end='\n\n')

yacko.set_link_node(dot)
dot.set_link_node(wacko)

print(yacko.link_node)  # link contains dot's node
print(wacko.link_node)  # doesn't have linked node, it will print None
print(dot.link_node, end='\n\n')  # link contains wacko's node

dots_data = yacko.get_link_node().get_value()
print("Dot's value:")
print(dots_data)

print(yacko.link_node.value)  # same to get linked-node's value

wackos_data = dot.get_link_node().get_value()
print("Wacko's value:")
print(wackos_data)

# Test case 2
print("\n---- Test case2 ----\n")
node1 = Node("This is my first node!")
node2 = Node("This is my second node!")
node3 = Node("This is my third node!")

node1.name = 'node1'
node2.name = 'node2'
node3.name = 'node3'

print(type(node1))
print(node1, end='\n\n')

print(node1.value)
print(node2.value)
print(node3.value)

print("")
node1.set_link_node(node2)
print(node1.link_node)
node2_data = node1.get_link_node().get_value()
print(node2_data)

print("")
print(node1.link_node)
print(node2.link_node)
print(node3.link_node)


