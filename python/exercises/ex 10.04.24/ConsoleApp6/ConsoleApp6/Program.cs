using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 2, 4, 7, 12 }

            public static boolean what(int[] arr, int num)
            {
                int k = 0;
                int p = arr.length - 1;
                int s;
                while (k < p)
                {
                    s = arr[k] + arr[p];
                    if (s < num)
                    {
                        k++;
                    }
                    else
                    {
                        if (s > num)
                        {
                            p--;
                        }
                        else
                        {
                            return true;
                        }
                    }
                }
                return false;
            }
            
        }
    }
}
