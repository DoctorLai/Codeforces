import java.io.*;
import java.util.*;

public class CodeForces268A
{
    public static void main(String[] args) throws IOException
    {
    		BufferedReader rr = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(rr.readLine());
		int[] h = new int[n];
		int[] a = new int[n];
		for (int i = 0; i < n; i ++)
		{
			String[] s = rr.readLine().split(" ");
			h[i] = Integer.parseInt(s[0]);
			a[i] = Integer.parseInt(s[1]);
		}
		int cnt = 0;
		for (int i = 0; i < n - 1; i ++)
		{
			for (int j = i + 1; j < n; j ++)
			{
				if (h[i] == a[j])
				{
					cnt ++;
				}
				if (h[j] == a[i])
				{
					cnt ++;
				}
			}
		}
		System.out.print(cnt);
    }
}