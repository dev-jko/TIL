import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Num1 {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String inputString = reader.readLine();
        reader.close();
        String[] arr = inputString.split(" ");

        Map<String, Integer> map = new HashMap<>();
        for (String s : arr) {
            int value = map.getOrDefault(s, 0);
            map.put(s, value + 1);
        }

        StringBuilder builder = new StringBuilder();

        Map<Integer, Integer> map2 = new HashMap<>();
        for (int value : map.values()) {
            int t = map2.getOrDefault(value, 0);
            map2.put(value, t + 1);
        }

        if (map2.size() == 1) {
            builder.append("Y\n");
        } else if (map2.size() == 2) {
            Integer[] t = new Integer[2];
            map2.keySet().toArray(t);
            if (t[0] < t[1]) {
                int tt = t[1];
                t[1] = t[0];
                t[0] = tt;
            }
            if (t[0] - t[1] == 1 && map2.get(t[1]) == 1) {
                builder.append("Y\n");
                n++;
            } else {
                builder.append("N\n");
            }
        } else {
            builder.append("N\n");
        }

        builder.append(n).append("\n")
                .append(map.size());
        System.out.println(builder.toString());
    }
}
