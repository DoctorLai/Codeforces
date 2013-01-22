import java.io.*;
import java.util.*;

public class Codeforces263D
{
    static int[] d;
    static int[] a;
    static List[] g;
    static boolean done = false;

    static void dfs(int v, int x, int k)
    {
        if (done)
        {
            return;
        }
        if (d[v] > 0)
        {
            if (x - d[v] > k)
            {
                System.out.println(x - d[v]);
                for (int i = d[v]; i < x; i ++)
                {
                    System.out.print(a[i] + " ");
                }
                done = true;
            }
            return;
        }
        d[v] = x;
        for (int i = 0; i < g[v].size(); i ++)
        {
            int cur = (Integer)g[v].get(i);
            a[x + 1] = cur;
            dfs(cur, x + 1, k);
        }
    }

    public static void main(String[] args) throws IOException
    {
        BufferedReader rr = new BufferedReader(new InputStreamReader(System.in));
        String[] s = rr.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        int k = Integer.parseInt(s[2]);
        g = new ArrayList[n + 1];
        a = new int[n + 2];
        d = new int[n + 1];
        for (int i = 0; i < n + 1; i ++)
        {
            g[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i ++)
        {
            s = rr.readLine().split(" ");
            int x = Integer.parseInt(s[0]);
            int y = Integer.parseInt(s[1]);
            g[x].add(y);
            g[y].add(x);
        }
        Arrays.fill(a, 0);
        Arrays.fill(d, 0);
        for (int i = 1; i < n + 1; i ++)
        {
            if (d[i] == 0)
            {
                a[1] = i;
                dfs(i, 1, k);
            }
        }
    }
}