import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solver extends SolverUtil {

  public void solve() throws Exception {
    String[] token = readLine().split(" ");
    int input = toInt(token[0]);

    int numLines = 0;
    for (int i = 0; i < numLines; i++) {
      token = readLine().split(" ");
    }

    println("= input =");
    println(input);
  }

  public static void main(String[] args) {
    try {
      Solver solver = new Solver();
      solver.setup();
      solver.solve();
      solver.cleanup();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

}

class SolverUtil {

  BufferedReader reader;
  BufferedWriter writer;

  public void setup() throws Exception {
    reader = new BufferedReader(new InputStreamReader(System.in));
    writer = new BufferedWriter(new OutputStreamWriter(System.out));
  }

  public void cleanup() throws Exception {
    reader.close();
    writer.flush();
    writer.close();
  }

  public String readLine() throws Exception {
    return reader.readLine();
  }

  public void println(String text) throws Exception {
    writer.write(text);
    writer.newLine();
  }

  public void println(int i) throws Exception {
    println(String.valueOf(i));
  }

  public int toInt(String text) {
    return Integer.parseInt(text);
  }
}
