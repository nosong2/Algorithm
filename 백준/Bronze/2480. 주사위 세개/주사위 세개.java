import java.io.*;
import java.util.*;

public class Main {
    public static int max(int a, int b, int c) {
        if (a > b && a > c) {
            return a;
        } else if (b > a && b > c) {
            return b;
        } else {
            return c;
        }
    }
    public static int check(int a, int b, int c) {
        if (a == b && a == c) {
            return 10000 + a * 1000;
        } else if (a == b && a != c || a == c && a != b) {
            return 1000 + a * 100;
        } else if (b == c && b != a) {
            return 1000 + b * 100;
        }
        else {
            return max(a, b, c) * 100;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int arr[] = new int[st.countTokens()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int answer;
        answer = check(arr[0], arr[1], arr[2]);

        bw.write(String.valueOf(answer));
        bw.flush();
        br.close();
        bw.close();
    }
}
