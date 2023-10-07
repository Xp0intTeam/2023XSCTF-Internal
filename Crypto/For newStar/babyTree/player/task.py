import hashlib
import sys
import uuid

class TreeNode(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

def Hash(data):
    first = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hashlib.sha256(first.encode('utf-8')).hexdigest()

def createTree(nodes):
    list_len = len(nodes)
    if list_len == 0:
        return 0
    else:
        while list_len %2 != 0:
            nodes.extend(nodes[-1:])
            list_len = len(nodes)
        secondary = []
        for k in [nodes[x:x+2] for x in range(0,list_len,2)]:
            newdata = Hash(k[0].data+k[1].data)         
            node = TreeNode(left=k[0],right=k[1],data=newdata)
            secondary.append(node)
        if len(secondary) == 1:
            return secondary[0]
        else:
            return createTree(secondary)
        
def Output_TreeHash(root, file):
    i=0
    queue = []
    queue.append(root)
    while(len(queue)>0):
        e = queue.pop(0)
        i+=1
        if e.left != None:
            queue.append(e.left)
        if e.right != None:
            queue.append(e.right)
        print(str(i),e.data, file=file)


if __name__ == "__main__":
    m = str(uuid.uuid4())
    flag = "flag{" + m + "}"
    blocks = flag.split("-") 
    nodes = [] 
    for element in blocks:
        d = Hash(element)
        nodes.append(TreeNode(data=d)) 
    root = createTree(nodes) 
    file = open('hash.txt', "w")
    print(flag, file=file)
    Output_TreeHash(root, file) 
    file.close()