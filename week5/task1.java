package week5;

public class task1 {
    public static void main(String[] args) {
        int[] numbers = { 1, 2, 3, 4, 5 };
        int sum = 0;

        for (int number : numbers) {
            sum += number;
        }

        System.out.println("The sum of the array elements is: " + sum);
    }

}

class ExpandableList {
    private int[] elements;
    private int size;
    private static final int INITIAL_CAPACITY = 10;

    public ExpandableList() {
        elements = new int[INITIAL_CAPACITY];
        size = 0;
    }

    public void add(int element) {
        if (size == elements.length) {
            resize();
        }
        elements[size++] = element;
    }

    private void resize() {
        int newCapacity = elements.length * 2;
        int[] newArray = new int[newCapacity];
        System.arraycopy(elements, 0, newArray, 0, elements.length);
        elements = newArray;
    }

    public int get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        return elements[index];
    }

    public int size() {
        return size;
    }
}