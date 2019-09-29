import jdk.jfr.Unsigned;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HelloWorld {
    public static void main(String[] args) throws IOException {

        long myLongLong = Long.MAX_VALUE;
        System.out.println(myLongLong);
        myLongLong = Long.MIN_VALUE;
        System.out.println(myLongLong);

        System.out.println("hello world");

        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }

        for (int i : arr) {
            System.out.println(i);
        }

        int[][] arrarr = new int[10][10];

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = Integer.parseInt(reader.readLine());
        }
        reader.close();


        StringBuilder builder = new StringBuilder();


    }

}