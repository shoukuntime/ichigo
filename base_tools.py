import itertools

ops = ['+', '-', '*', '/']

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_expr(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return f'({self.left.to_expr()}{self.val}{self.right.to_expr()})'

# 建立所有表達式樹
def build_all_expr_trees(tokens):
    if len(tokens) == 1:
        return [Node(tokens[0])]

    trees = []
    for i in range(1, len(tokens)-1, 2):
        op = tokens[i]
        left_tokens = tokens[:i]
        right_tokens = tokens[i+1:]

        left_trees = build_all_expr_trees(left_tokens)
        right_trees = build_all_expr_trees(right_tokens)

        for lt in left_trees:
            for rt in right_trees:
                trees.append(Node(op, lt, rt))
    return trees

def function(nums: list, tar=15) -> str:
    n = len(nums)
    for num_perm in itertools.permutations(nums):
        for ops_perm in itertools.product(ops, repeat=n-1):
            tokens = []
            for i in range(n-1):
                tokens.append(num_perm[i])
                tokens.append(ops_perm[i])
            tokens.append(num_perm[-1])

            expr_trees = build_all_expr_trees(tokens)
            for tree in expr_trees:
                expr = tree.to_expr()
                try:
                    if abs(eval(expr) - tar) < 1e-6:
                        return expr + f"={tar}"
                except ZeroDivisionError:
                    continue
    return f"無法達成{tar}"

print(function([1, 2, 3, 4, 5]))