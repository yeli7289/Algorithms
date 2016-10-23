class Tree(object):
	def __init__(self, x):
			self.val=x
			self.left=None
			self.right=None

def dfsAncestor(root, node, path):
	if not root:
		return False
	if root.val==node:
		return True
	ret = dfsAncestor(root.left, node, path) or dfsAncestor(root.right, node, path)
	if ret:
		path.append(root.val)
	return ret
def LCA(root, node1, node2):
	path1 = []
	path2 = []
	if dfsAncestor(root, node1, path1) and dfsAncestor(root, node2, path2):
		path1, path2 = path1[::-1], path2[::-1]
		i=0
		while i <len(path1) and i < len(path2):
			if  path1[i]!=path2[i]:
				break
			i+=1
		return path1[i-1]
	else:
		return -1
if __name__ == "__main__":
	root=Tree('A')
	root.left=Tree('B')
	root.right=Tree('C')
	root.left.left=Tree('D')
	root.left.right=Tree('E')

	node1='D'
	node2='E'
	node = LCA(root, node1, node2)
	print node
	


