package week2;

public class exercise10 {
    public static void main(String[] args) {
        ExtendableList<String> list = new ExtendableList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");

        System.out.println("List size: " + list.size()); // Output: List size: 3
        System.out.println("Item at index 1: " + list.get(1)); // Output: Item at index 1: Banana

        list.remove(1);
        System.out.println("List size after removal: " + list.size()); // Output: List size after removal: 2
        System.out.println("Item at index 1 after removal: " + list.get(1)); // Output: Item at index 1 after removal:
    }
}

class ExtendableList<T> {
    private T[] items;
    private int size;
    private static final int INITIAL_CAPACITY = 1;

    // SuppressWarnings is used to avoid unchecked cast warning from Object[] to T[]
    @SuppressWarnings("unchecked")
    public ExtendableList() {
        items = (T[]) new Object[INITIAL_CAPACITY];
        size = 0;
    }

    public void add(T item) {
        if (size == items.length) {
            extendCapacity();
        }
        items[size] = item;
        size++;
    }

    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        return items[index];
    }

    public int size() {
        return size;
    }

    public void remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        // Shift elements to the left to fill the gap
        for (int i = index; i < size - 1; i++) {
            items[i] = items[i + 1];
        }
        items[size - 1] = null; // Clear the last element
        size--;
    }

    @SuppressWarnings("unchecked")
    private void extendCapacity() {
        int newCapacity = items.length * 2;
        T[] newItems = (T[]) new Object[newCapacity];
        for (int i = 0; i < items.length; i++) {
            newItems[i] = items[i];
        }
        items = newItems;
    }

}