//http://www.codeforces.com/problemset/problem/230/B
//http://www.zhihua-lai.com/acm

import java.util.Scanner;

public class Codeforces230B
{
	private static boolean Prime(long k)
	{
		long u = (long)Math.round(Math.sqrt(k));
		long c = 1;
		for (long i = 2; i <= u; i += c)
		{
			if (k % i == 0)
			{
				return (false);
			}
			if (i == 3)
			{
				c = 2;
			}
		}
		return (true);
	}

    public static void main(String[] args)
    {
		Scanner in = new Scanner(System.in);
		long n = in.nextLong();
		for (int i = 0; i < n; i ++)
		{
			long k = in.nextLong();
			long u = (long)Math.sqrt(k);
			if ((k > 1) && (u * u == k) && Prime(u))
			{
				System.out.println("YES");
			}
			else
			{
				System.out.println("NO");
			}
		}
    }
}
