import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Num4 {

    static Map<String, Integer> city = makeCityIndex();
    static int[][] graph;

    public static void main(String[] args) throws Exception {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] t = reader.readLine().split(" ");
        int n = Integer.parseInt(t[0]);
        int k = Integer.parseInt(t[1]);
        int en = Integer.parseInt(reader.readLine());
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = -1;
            }
        }
        for (int i = 0; i < en; i++) {
            t = reader.readLine().split(" ");
            graph[city.get(t[0])][city.get(t[1])] = Integer.parseInt(t[2]);
            graph[city.get(t[1])][city.get(t[0])] = Integer.parseInt(t[2]);
        }
        reader.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(graph[i][j] + "\t");
            }
            System.out.println();
        }


        MyResult[][] result = new MyResult[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = new MyResult()
            }
        }
        boolean[] visited = new boolean[n];
        visited[0] = true;
        int money = 0;
        dfs(0, 30, money, visited, result);


        StringBuilder builder = new StringBuilder();
    }

    private static void dfs(int currentCity, int k, int money, boolean[] visited, MyResult[][] result){
        if (currentCity != graph.length - 1) {
            money += 200;
            for (int i = 0; i < graph.length; i++) {
                if (graph[currentCity][i] >= 0 && !visited[i]) {
                    visited[i] = true;
                    result[currentCity][i].setPath(i);
                    dfs(i,k -graph[currentCity][i], money, visited, result);
                    visited[i] = false;
                }
            }

        }

    }


    class MyResult{
        private String path = "";
        private int money = 0;
        private int k = 0;

        public String getPath() {
            return path;
        }

        public void setPath(String path) {
            this.path += " " + path;
        }

        public int getMoney() {
            return money;
        }

        public void setMoney(int money) {
            this.money = money;
        }

        public int getK() {
            return k;
        }

        public void setK(int k) {
            this.k = k;
        }
    }


    private static Map<String, Integer> makeCityIndex() {
        Map<String, Integer> city = new HashMap();
        city.put("A", 0);
        city.put("B", 1);
        city.put("C", 2);
        city.put("D", 3);
        city.put("E", 4);
        city.put("F", 5);
        city.put("G", 6);
        city.put("H", 7);
        city.put("I", 8);
        city.put("J", 9);
        city.put("K", 10);
        city.put("L", 11);
        city.put("M", 12);
        city.put("N", 13);
        city.put("O", 14);
        city.put("P", 15);
        city.put("Q", 16);
        city.put("R", 17);
        city.put("S", 18);
        city.put("T", 19);
        city.put("U", 20);
        city.put("V", 21);
        city.put("W", 22);
        city.put("X", 23);
        city.put("Y", 24);
        city.put("Z", 25);
        return city;
    }


}
