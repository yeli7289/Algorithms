# cracking the coding interview 4.9
# find all possible combination of a BST in array.
class Tree(object):
	def __init__(self, x):
 		self.val=x
 		self.left=None
 		self.right=None
def BSTSequence(root):
	ret=[]
	dfs([],ret,[root])
	return ret

def dfs(path, ret, Q):
	if not Q:
		ret.append(path)
		return
	i=0
	while i<len(Q):
		n = Q.pop(i)
		left = [n.left] if n.left else []
		right = [n.right] if n.right else []
		dfs(path+[n.val], ret, left+right+Q)
		Q.insert(i, n)
		i+=1
root=Tree(50)
root.left=Tree(20)
root.right=Tree(60)
root.left.left=Tree(10)
root.left.right=Tree(25)
# root.left.left.left=Tree(5)
# root.left.left.right=Tree(15)
root.right.right=Tree(70)
# root.right.right.left=Tree(65)
# root.right.right.right=Tree(80)

AllPath = BSTSequence(root)
print AllPath