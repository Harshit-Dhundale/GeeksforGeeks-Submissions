import sys
sys.setrecursionlimit(10**5)
class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        inorder = []
        
        def DFS(root):
            if root is None:
                return
            # skip_flag = 0
            DFS(root.left)
            
            if root.left is None and root.right is not None:
                # parent = root.left
                # skip_flag = 1
                pass
            elif root.right is None and root.left is not None:
                # parent = root.right
                # skip_flag = 1
                pass
            else:
                nonlocal inorder
                inorder.append(root.data)
            
            DFS(root.right)
        
        DFS(node)
        # print(inorder)
        # node = n = Node()
        prev = n = Node(inorder.pop())
        while inorder:
            data = inorder.pop()
            node = Node(data)
            prev.left = node
            prev = node
        return n


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = Node(int(ip[0]))

    queue = []
    queue.append(root)

    i = 1
    while len(queue) > 0 and i < len(ip):
        currNode = queue.pop(0)
        currVal = ip[i]

        if currVal != 'N':
            currNode.left = Node(int(currVal))
            queue.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != 'N':
            currNode.right = Node(int(currVal))
            queue.append(currNode.right)

        i += 1

    return root


def printInorder(root):
    if root is None:
        return

    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1

    while t > 0:
        s = data[index]
        root = buildTree(s)
        solution = Solution()
        fresh = solution.RemoveHalfNodes(root)
        printInorder(fresh)
        print()
        t -= 1
        index += 1

# } Driver Code Ends