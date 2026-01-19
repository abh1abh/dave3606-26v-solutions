public class ExpressionTree {
    // Exercise 7a and 7b.
    public static int evaluate(Node node) {
        if (node.number != null) {
            return node.number;
        }
        String op = node.operator;

        // Optional special case: unary minus only has a right child.
        // Therefore, we perform the "right" recursive call first,
        // since that operand is always there. If we had not needed to
        // support unary operators, we could have performed the "left"
        // recursive call first.
        int right = evaluate(node.rightChild);
        if (op.equals("-") && node.leftChild == null) {
            return -right;
        }

        int left = evaluate(node.leftChild);

        if (op.equals("+")) {
            return left + right;
        } else if (op.equals("-")) {
            return left - right;
        } else if (op.equals("*")) {
            return left * right;
        } else if (op.equals("/")) {
            return left / right;
        } else if (op.equals("^")) {
            // Supporting this operator was optional.
            return (int) Math.pow(left, right);
        }
        else {
            throw new IllegalArgumentException("Invalid operator: " + op);
        }
    }

    // Exercise 7e.
    private static final Map<String, Integer> precedence = Map.of(
        "+", 0,
        "-", 0,
        "*", 1,
        "/", 1,
        "^", 2
    );

    public static void printExpressionTree(Node node, String parentOperator) {
        boolean needsParentheses =
            parentOperator != null &&
            node.operator != null &&
            precedence.get(node.operator) < precedence.get(parentOperator);

        if (needsParentheses) {
            System.out.print("(");
        }

        if (node.leftChild != null) {
            printExpressionTree(node.leftChild, node.operator);
        }

        System.out.print(node);

        if (node.rightChild != null) {
            printExpressionTree(node.rightChild, node.operator);
        }

        if (needsParentheses) {
            System.out.print(")");
        }
    }
}
