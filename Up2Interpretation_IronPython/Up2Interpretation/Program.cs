using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;

using dotnetlib1;

namespace Up2Interpretation
{
    class Program
    {
        static private ScriptEngine engine;
        static private ScriptScope scope;

        static void Main(string[] args)
        {
            engine = Python.CreateEngine();

            engine.Runtime.LoadAssembly(typeof(dotnetlib1.Up2InterpretationCls).Assembly);
            
            scope = engine.CreateScope();
            engine.Execute("import dotnetlib1", scope);
            engine.Execute("dotnetlib1.Up2InterpretationCls.WriteAllToConsole('val: {}'.format(v) for v in range(20))", scope);
        }
    }
}
