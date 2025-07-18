import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[t];
        int ysum = 0, msum = 0;
        for (int i = 0; i < t; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 영식 30 / 10
        for (int i = 0; i < t; i++) {
            ysum = ysum + arr[i]/30 + 1;
        }
        
        // 민식 60 / 15
        for (int i = 0; i < t; i++) {
            msum = msum + arr[i]/60 + 1;
        }

        if (ysum * 10 < msum * 15) {
            bw.write("Y ");
            bw.write(String.valueOf(ysum * 10));
        } else if (msum * 15 < ysum * 10) {
            bw.write("M ");
            bw.write(String.valueOf(msum * 15));
        } else {
            bw.write("Y M ");
            bw.write(String.valueOf(ysum * 10));
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
