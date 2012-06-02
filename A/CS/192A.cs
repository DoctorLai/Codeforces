using System;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            n *= 2;
            int k = (int)Math.Sqrt(n);
            bool found = false;
            for (int i = 1; i < k; i++)
            {
                int r = n - i * i - i;
                int x = (int)Math.Sqrt(r);
                if (x * (x + 1) == r)
                {
                    found = true;
                    break;
                }
            }
            if (found)
            {
                Console.Write("YES");
            }
            else
            {
                Console.Write("NO");
            }
            //Console.ReadLine();
        }
    }
}
