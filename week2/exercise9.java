package week2;

public class exercise9 {
    public static void main(String[] args) {
        String[] items = {
                "apple",
                "banana",
                "cherry",
                "date",
                "elderberry"
        };

        String html = buildHtmlList(items);
        System.out.println(html);
    }

    public static String buildHtmlList(String[] items) {
        StringBuilder html = new StringBuilder(); // O(1)
        html.append("<ul>\n"); // O(1)
        for (String item : items) { // n iterations
            html.append("  <li>"); // O(1) each time, O(n) total
            html.append(item); // O(k) each time, O(nk) total
            html.append("</li>\n"); // O(1) each time, O(n) total
        }
        html.append("</ul>"); // O(1)
        return html.toString(); // O(nk)

        // Total: O(nk)
    }
}
