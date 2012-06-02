import java.util.Scanner;

public class CodeForces192A
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        n *= 2;
        int k = (int)Math.round(Math.sqrt(n));
        boolean found = false;
        for (int i = 1; i < k; i ++)
        {
            int r = n - i * i - i;
            int x = (int)Math.sqrt(r);
            if (x * (x + 1) == r)
            {
                found = true;
                break;
            }
        }
        if (found)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}