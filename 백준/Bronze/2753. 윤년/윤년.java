import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int answer = 0;
        if (a % 400 == 0 || a % 4 == 0 && a % 100 != 0) {
            answer = 1;
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        br.close();
        bw.close();
    }
}
