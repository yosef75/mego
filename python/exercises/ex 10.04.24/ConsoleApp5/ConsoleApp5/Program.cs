using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp6
{
    internal class Program
    {
        static void F(int x)

        {
            if (x > 0)
            {
                if (x % 2 == 0)
                {
                    
                    for (int i = 0; i < (x % 10) ; i++) 
                    {
                        Console.Write(x % 10);
                    }
                    Console.WriteLine();
                }
                F(x / 10);
                if (x % 2 == 1) 
                {
                    
                    for (int i = 0; i < (x % 10); i++)
                    {
                        Console.Write('*');
                    }
                         
                }
                        
                }
        }
        
        static void Main(string[] args)
        {
            F(84265841);
        }
    }
}


