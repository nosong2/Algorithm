import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a, sum = 0, max = 100;
        for (int i = 0; i < 7; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            a = Integer.parseInt(st.nextToken());
            if (a % 2 == 1) {
                sum += a;
                if (a < max) {
                    max = a;
                }
            }
        }
        if (sum == 0) {
            bw.write("-1");
        } else {
            bw.write(String.valueOf(sum));
            bw.newLine();
            bw.write(String.valueOf(max));
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
