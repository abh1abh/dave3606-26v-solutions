package week3;

import java.util.List;

public class Exercise3 {
    public static void main(String[] args) {
        List<Integer> values = List.of(1, 2, 3, 4, 5, 6);
        List<Integer> result = streamExample(values);
        System.out.println(result);
    }

    public static List<Integer> streamExample(List<Integer> values) {
        return values.stream()
                .filter(v -> v % 2 == 0)
                .map(v -> v * v)
                .toList();
    }
}
