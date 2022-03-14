package com.stephenlhc;

public class InvertBinaryTree {
    // 226. Invert Binary Tree

    public TreeNode invertTree(TreeNode root) {
        if(root == null) return null;

        var left = root.left;
        var right = root.right;
        root.left = right;
        root.right = left;

        invertTree(root.left);
        invertTree(root.right);

        return root;
    }
}
