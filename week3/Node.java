package analysis;

import java.util.List;

public class Node {
    private final Integer number;
    private final String operator;
    private final Node leftChild;
    private final Node rightChild;

    private static final List<String> validOperators = List.of("+", "-", "*", "/");

    Node(int number) {
        this.number = number;
        this.operator = null;
        this.leftChild = null;
        this.rightChild = null;
    }

    Node(String operator, Node rightChild) {
        // Call the other constructor.
        this(operator, null, rightChild);
    }

    Node(String operator, Node leftChild, Node rightChild) {
        if (operator == null || !validOperators.contains(operator)) {
            throw new IllegalArgumentException("Invalid operator: " + operator);
        } else if (rightChild == null) {
            throw new IllegalArgumentException("Missing right operand");
        } else if (leftChild == null && !operator.equals("-")) {
            throw new IllegalArgumentException("Missing left operand");
        }
        this.number = null;
        this.operator = operator;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    @Override
    public String toString() {
        if (operator != null) {
            return operator;
        } else {
            return number.toString();
        }
    }
}
