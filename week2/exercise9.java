
public class exercise9 {
    public static void main(String[] args) {
        
    }

    public static String buildHtmlList(String[] items) {
        StringBuilder htmlList = new StringBuilder(); 
        htmlList.append("<ul>\n"); // O(1)
        for (String item : items) { // O(n)
            htmlList.append("  <li>").append(item).append("</li>\n"); // O(1)
        }
        htmlList.append("</ul>"); // O(1)
        return htmlList.toString();  // O(n)
    }
}
