using System;

namespace MediatorDemoSimple
{
    // Remove the word Simple to run
    class Program
    {
        static void Main(string[] args)
        {
            var mediator = new ConcreteMediator();
            /*var c1 = new Colleague1();
            var c2 = new Colleague2();
            mediator.Register(c1);
            mediator.Register(c2);
            */

            /*mediator.colleague1 = c1;
            mediator.colleague2 = c2;*/

            var c1 = mediator.CreateColleague<Colleague1>();
            var c2 = mediator.CreateColleague<Colleague2>();


            c1.Send("Hello World from C1"); 
            c2.Send("Hi from c2");
        }
    }
}
