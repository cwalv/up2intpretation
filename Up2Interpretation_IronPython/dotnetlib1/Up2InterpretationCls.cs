using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dotnetlib1
{
    public class Up2InterpretationCls
    {
        public static void WriteToConsole(Object o)
        {
            Console.Out.WriteLine(o.ToString());
        }

        public static void WriteAllToConsole(IEnumerable<Object> oGenerator)
        {
            foreach (var o in oGenerator)
            {
                WriteToConsole(o);
            }
        }

    }
}
