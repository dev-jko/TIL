import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Num2 {


    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[][] inputs = new String[n][];
        for (int i = 0; i < n; i++) {
            inputs[i] = reader.readLine().split(" ");

        }
        reader.close();

        Map<String, Integer> map = new HashMap<>();
        PriorityQueue<String> pq = new PriorityQueue<>((o1, o2) -> map.get(o2) - map.get(o1));
        StringBuilder builder = new StringBuilder();

        for (String[] in : inputs) {
            if (in[0].charAt(0) == 'e') {
                String k = in[1];
                if (map.containsKey(k)) {
                    pq.remove(k);
                }
                int value = map.getOrDefault(k, 0);
                map.put(k, value + 1);
                pq.offer(k);
            } else if (pq.size() > 0) {
                String k = pq.poll();
                int value = map.get(k);
                if (value > 1) {
                    map.put(k, value - 1);
                    pq.offer(k);
                } else {
                    map.remove(k);
                }
                builder.append(k).append(" ");
            } else {
                builder.append(-1).append(" ");
            }
        }

        System.out.println(builder.toString());
    }

}
