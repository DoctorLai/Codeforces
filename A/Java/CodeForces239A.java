//http://www.zhihua-lai.com/acm

import java.util.*;
import java.io.*;

public class CodeForces239A
{
    public static void main(String[] args) throws IOException
    {
		BufferedReader rr = new BufferedReader(new InputStreamReader(System.in));
		String[] s = rr.readLine().split(" ");
		int y = Integer.parseInt(s[0]);
		int k = Integer.parseInt(s[1]);
		int n = Integer.parseInt(s[2]);
		int x = k - (y % k);
		if (x + y > n)
		{
			System.out.print(-1);
		}
		else
		{
			while (x + y <= n)
			{
				System.out.print(x + " ");
				x += k;
			}
		}
    }
}