from BSTree import BSTree

def main():
    tree = BSTree()
    arr = [4,2,12,11,8,9,1,13,20,7,7]
    for i in arr:
        tree.addNode(tree.create(i))
    
    #tree.inorder(tree.root)
    tree.preorder(tree.root)
    print tree.depth(tree.root)
    #tree.postorder(tree.root)

if __name__=='__main__':
    main()