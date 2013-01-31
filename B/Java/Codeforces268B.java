import java.io.*;
import java.util.*;

public class Codeforces268B
{
	static int solve(int n)
	{
		if (n == 1) return 1;
		if (n == 2) return 3;
		int cnt = 0;
		for (int i = 1; i <= n; i ++)
		{
			cnt += i * (n - i + 1) - (i - 1);
		}
		return cnt;
	}

	public static void main(String[] args) throws IOException
	{
		BufferedReader rr = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(rr.readLine());
		System.out.print(solve(n));
	}
}