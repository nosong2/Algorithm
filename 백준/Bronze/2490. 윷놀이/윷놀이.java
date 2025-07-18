import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int a;
        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int counts = 0;
            for (int j = 0; j < 4; j++) {
                a = Integer.parseInt(st.nextToken());
                if (a == 1) {
                    counts += 1;
                }
            }
            if (counts == 0) {
                bw.write("D");
            } else if (counts == 1) {
                bw.write("C");
            } else if (counts == 2) {
                bw.write("B");
            } else if (counts == 3) {
                bw.write("A");
            } else if (counts == 4) {
                bw.write("E");
            }
            bw.newLine();
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
