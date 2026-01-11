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
        StringBuilder htmlList = new StringBuilder();
        htmlList.append("<ul>\n"); // O(1)
        for (String item : items) { // n iterations
            htmlList.append("  <li>").append(item).append("</li>\n"); // O(1) in each iteration; O(n) in total
        }
        htmlList.append("</ul>"); // O(1)
        return htmlList.toString(); // O(n)
    }
}
