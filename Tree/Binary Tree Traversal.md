# Binary Tree Preorder Traversal (Iterative)
# Code
```
def preOrderTraversal(root):
	if not root:
		return []
	stack = [root]
	result = []
	while stack:
		node = stack.pop()
		result.append(node.val)
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
	return result
```
# Binary Tree postOrder Traversal (Iterative)
# Code
```
def postOrderTraversal(root):
	if not root:
		return []
	stack = [root]
	result = []
	node = root
	while stack:
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)
		node = stack.pop()
		result.append[node.val]
	return result
```
# Binary Tree InOrder Traversal (Iterative)
# Code
```
def inOrderTraversal(root):
	if not root:
		return []
	stack = []
	result = []
	node = root
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			result.append(node.val)
			node = node.right
	return result
```