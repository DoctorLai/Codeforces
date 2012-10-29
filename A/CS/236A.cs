using System;
using System.Collections.Generic;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            HashSet<char> aa = new HashSet<char>();
            string s = Console.ReadLine();
            foreach (char ch in s)
            {
                if (!aa.Contains(ch))
                {
                    aa.Add(ch);
                }
            }
            Console.Write((aa.Count & 1) == 0 ? "CHAT WITH HER!" : "IGNORE HIM!");
        }
    }
}
