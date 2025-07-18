import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int arr[] = new int[9];
        int slot, sum=0;
        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            arr[i] = Integer.parseInt(st.nextToken());
            sum += arr[i];
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 1; j < 9; j++) {
                if (100 == sum - (arr[i] + arr[j])) {
                    arr[i] = arr[j] = 0;
                }
                if (arr[j] == 0) break;              
            }
            if (arr[i] == 0) break;
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 8; j++) {
                if (arr[j] > arr[j + 1]) {
                    slot = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = slot;
                }
            }
        }

        for (int i = 2; i < 9; i++) {
            bw.write(String.valueOf(arr[i]));
            bw.newLine();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
