import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int arr[] = new int[5];
        int slot, sum=0;
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            arr[i] = Integer.parseInt(st.nextToken());
            sum += arr[i];
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 4; j++) {
                if (arr[j] > arr[j + 1]) {
                    slot = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = slot;
                }
            }
        }

        bw.write(String.valueOf(sum / 5));
        bw.newLine();
        bw.write(String.valueOf(arr[2]));

        bw.flush();
        br.close();
        bw.close();
    }
}
