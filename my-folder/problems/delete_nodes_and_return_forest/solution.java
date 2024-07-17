/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        // convert to_delete to a hash set
        Set<Integer> toDeleteSet = new HashSet<>();
        for(int val : to_delete){
            toDeleteSet.add(val);
        } 

        // create result to return
        List<TreeNode> result = new ArrayList<>();

        // traverse through root and find nodes to delete using helper function
        root = helper(root, toDeleteSet, result);

        // if root is not null, add it to result
        if(root != null){
            result.add(root);
        }

        return result;
    }

    // create helper function to traverse through nodes
    private TreeNode helper(TreeNode node, Set<Integer> toDeleteSet, List<TreeNode> result){
        if(node == null){
            return null;
        }

        // call recursively by passing each node into the helper function
        node.left = helper(node.left, toDeleteSet, result);
        node.right = helper(node.right, toDeleteSet, result);

        // check if value is in delete set
        if(toDeleteSet.contains(node.val)){
            // check if node has children
            if(node.left != null){
                result.add(node.left);
            }
            if(node.right != null){
                result.add(node.right);
            }
            return null;
        }

        return node;

    }
}  