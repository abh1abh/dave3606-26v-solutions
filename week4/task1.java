package week4;

public class task1 {
    public static void main(String[] args) {
        // Divided by 8 to convert bits to bytes
        System.out.println("Integer types");
        System.out.println("byte:   " + (Byte.SIZE / 8) + " byte");
        System.out.println("short:  " + (Short.SIZE / 8) + " bytes");
        System.out.println("int:    " + (Integer.SIZE / 8) + " bytes");
        System.out.println("long:   " + (Long.SIZE / 8) + " bytes");
        System.out.println("char:   " + (Character.SIZE / 8) + " bytes");

        System.out.println("\nFloating-points");
        System.out.println("float:  " + (Float.SIZE / 8) + " bytes");
        System.out.println("double: " + (Double.SIZE / 8) + " bytes");
        System.out.println("\nOther types");
        System.out.println("boolean: (no fixed SIZE constant in Java)");
    }
}
