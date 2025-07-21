import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String n = br.readLine();
        int t = Integer.parseInt(br.readLine());

        Deque<Character> left = new ArrayDeque<>();
        Deque<Character> right = new ArrayDeque<>();

        for (int i = 0; i < n.length(); i++) {
            left.addLast(n.charAt(i));
        }

        for (int i = 0; i < t; i++) {
            String command = br.readLine();
            char cmd = command.charAt(0);

            if (cmd == 'L' && !left.isEmpty()) {
                right.addFirst(left.removeLast());
            } else if (cmd == 'D' && !right.isEmpty()) {
                left.addLast(right.removeFirst());
            } else if (cmd == 'B' && !left.isEmpty()) {
                left.removeLast();
            } else if (cmd == 'P') {
                char c = command.charAt(2);
                left.addLast(c);
            }
        }

        for (char ch : left) {
            bw.write(ch);
        }
        for (char ch : right) {
            bw.write(ch);
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
