import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int arr[] = new int[20];
        int slot;
        for (int i = 0; i < 20; i++) {
            arr[i] = i + 1;
        }

        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());

            for (int j = 0; j < (second - first)/2 + 1; j++) {
                slot = arr[first + j - 1];
                arr[first + j - 1] = arr[second - j - 1];
                arr[second - j - 1] = slot;
            }
        }
        for (int i = 0; i < 20; i++) {
            bw.write(String.valueOf(arr[i]) + " ");
        }



        bw.flush();
        br.close();
        bw.close();
    }
}
