import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int main = 1;
        int arr[] = new int[10];
        for (int i = 0;i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            main = main * Integer.parseInt(st.nextToken());
        }
        while (main > 0) {
            arr[main%10]++;
            main /= 10;
        }
        for (int i = 0;i < 10;i++) {
            bw.write(String.valueOf(arr[i]));
            bw.newLine();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
