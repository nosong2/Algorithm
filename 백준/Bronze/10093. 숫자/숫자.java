import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long slot, cnt;
        if (a > b) {
            slot = a;
            a = b;
            b = slot;
        }
        if (a == b) {
            cnt = 0;
        } else {
            cnt = b - a - 1;
        }
        bw.write(String.valueOf(cnt));
        bw.newLine();
        for (int i = 0; i < cnt; i++) {
            bw.write(String.valueOf(a + i + 1) + " ");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
