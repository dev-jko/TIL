public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("hello world");

        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }

        for (int i : arr) {
            System.out.println(i);
        }
    }

}