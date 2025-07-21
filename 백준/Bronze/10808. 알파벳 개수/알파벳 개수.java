import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        String n = String.valueOf(st.nextToken());
        int arr[] = new int[26];

        for (int i = 0; i < n.length(); i++) {
            int ascii = (int) n.charAt(i);
            arr[ascii - 97]++;
        }

        for (int i = 0; i < 26; i++) {
            bw.write(String.valueOf(arr[i]) + " ");
        }


        bw.flush();
        br.close();
        bw.close();
    }
}
