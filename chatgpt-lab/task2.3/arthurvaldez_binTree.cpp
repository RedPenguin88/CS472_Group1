/****************************
 *    CS 302 Assignment 4   *
 *                          *
 *  Arthur Ethan Valdez III *
 * **************************/

/*
 *         Name: Arthur Ethan Valdez, 2001802124
 *  Description: This program creates a binary tree based on user input, and finds the longest
 *               zigzag path.
 *        Input: The program requires user inputs.
 *       Output: The program is expected the path with the longest zigzag.
 */

#include <vector>
#include <string>
#include <iostream>

struct binTreeNode
{
	std::string location;
	binTreeNode * left;
	binTreeNode * right;
};

class binTree
{	
public:
	binTree();
	~binTree();
	void buildTree(std::vector<std::string>);
	std::vector<std::string> zigzag();
    //binTreeNode * getRoot();
    //void printPreorder( binTreeNode * node);
    
    
private:
	binTreeNode* buildTree(binTreeNode *, std::vector<std::string>, int);
    std::vector<std::string> binTree::zigzagLeft(binTreeNode* r, std::vector<std::string>& path);
    std::vector<std::string> binTree::zigzagRight(binTreeNode* r, std::vector<std::string>& path);
	void deallocateTree(binTreeNode*);
	binTreeNode* root;
};

binTree::binTree()
{
	root = nullptr;
}

binTree::~binTree(){
    deallocateTree(root);
}

/*
 *  deallocateTree(): Deallocates the binary tree.
 *  parameters: binTreeNode * r - node to be passed in
 *  return value: Void.
 *  Algorithm: Recursively calls itself to delete both sides of the tree until finally
 *             deleting the root node.
 */
void binTree::deallocateTree(binTreeNode * r)
{
	if(r == NULL)
        return;
    
    deallocateTree(r->left);
    deallocateTree(r->right);

    delete r;
}

/*
 *  buildTree(): Constructs the binary tree.
 *  parameters: std::vector<std::string> locations - vector to create the binary tree
 *  return value: Void.
 *  Algorithm: If locations is empty, it returns. Otherwise, calls an overloaded function of
 *             itself.
 */
void binTree::buildTree(std::vector<std::string> locations)
{
	if(locations.size() == 0)
		return;
	root = buildTree(new binTreeNode(), locations, 0);
}

/*
 *  buildTree(): Constructs the binary tree.
 *  parameters: binTreeNode * r - node to be passed in
 *              std::vector<std::string> locations - vector to create the binary tree
 *              int index - the current position in the vector
 *  return value: Returns a binTreeNode.
 *  Algorithm: Returns nullptr and deletes the node if out of bounds or if the string in the vector is equal to "=.
 *             Otherwise, it recursively calls itself and assigns nodes locations based on these algorithms:
 *             index * 2 + 1 and (index + 1) * 2.
 */
binTreeNode* binTree::buildTree(binTreeNode * r, std::vector<std::string> locations, int index)
{
    //Base cases
    if(index < locations.size() && index > -1)
    {
        r->location = locations[index];
        if(r->location == "_")
        {
            delete r;
            return nullptr;
        }
        r->left = buildTree(new binTreeNode(), locations, index * 2 + 1);
        r->right = buildTree(new binTreeNode(), locations, (index + 1) * 2);
    }
    else
    {
        delete r;
        return nullptr;
    }
    return r;
}


/*
 *  zigzagLeft(): Performs a left zigzag traversal from the given node.
 *  parameters: binTreeNode* r - node to start the traversal from
 *              std::vector<std::string>& path - the current zigzag path (modified during traversal)
 *  return value: Returns a string vector representing the longest left zigzag path.
 *  Algorithm: Recursively traverses the left subtree, appends node locations to the provided path vector,
 *             and compares the lengths of the resulting left zigzag paths.
 */
std::vector<std::string> binTree::zigzagLeft(binTreeNode* r, std::vector<std::string>& path)
{
    if (r == nullptr)
        return std::vector<std::string>();

    path.push_back(r->location);

    std::vector<std::string> leftPath = zigzagLeft(r->left, path);
    std::vector<std::string> rightPath = zigzagLeft(r->right, std::vector<std::string>());

    return (leftPath.size() > rightPath.size()) ? leftPath : rightPath;
}

/*
 *  zigzagRight(): Performs a right zigzag traversal from the given node.
 *  parameters: binTreeNode* r - node to start the traversal from
 *              std::vector<std::string>& path - the current zigzag path (modified during traversal)
 *  return value: Returns a string vector representing the longest right zigzag path.
 *  Algorithm: Recursively traverses the right subtree, appends node locations to the provided path vector,
 *             and compares the lengths of the resulting right zigzag paths.
 */
std::vector<std::string> binTree::zigzagRight(binTreeNode* r, std::vector<std::string>& path)
{
    if (r == nullptr)
        return std::vector<std::string>();

    path.push_back(r->location);

    std::vector<std::string> leftPath = zigzagRight(r->left, std::vector<std::string>());
    std::vector<std::string> rightPath = zigzagRight(r->right, path);

    return (leftPath.size() > rightPath.size()) ? leftPath : rightPath;
}

/*
 *  zigzag(): Initiates both left and right zigzag traversals from the root.
 *  parameters: None.
 *  return value: Returns a string vector representing the longest zigzag path overall.
 *  Algorithm: Calls the zigzagLeft and zigzagRight functions from the root, compares the lengths of
 *             resulting zigzag paths, and returns the vector with the longest zigzag path.
 */
std::vector<std::string> binTree::zigzag()
{
    std::vector<std::string> vector1; 
    std::vector<std::string> leftZag = zigzagLeft(root, vector1);
    std::vector<std::string> rightZag = zigzagRight(root, vector1);

    if (leftZag.size() + rightZag.size() == 0)
        return vector1;
    return (leftZag.size() > rightZag.size()) ? leftZag : rightZag;
}

/*

binTreeNode * binTree::getRoot()
{
    return root;
}

// Given a binary tree, print its nodes in inorder
void binTree::printPreorder(binTreeNode * node)
{
    if (node == NULL)
        return;
 
    //first print data of node
    std::cout << node->location << " ";
 
    //then recur on left subtree
    printPreorder(node->left);
 
    // now recur on right subtree
    printPreorder(node->right);
}*/


//binTreeNode* binTree::getRoot()
//{
//    return root;
//}