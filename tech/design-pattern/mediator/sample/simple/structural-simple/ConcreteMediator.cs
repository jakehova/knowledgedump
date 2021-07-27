using System;
using System.Collections.Generic;
using System.Linq;

namespace MediatorDemoSimple
{
    public class ConcreteMediator : Mediator
    {
        /*public Colleague1 colleague1 {get;set;}
        public Colleague2 colleague2 {get;set;}*/

        public List<Colleague> colleagues = new List<Colleague>();

        public void Register (Colleague colleague){
            colleague.SetMediator(this);
            this.colleagues.Add(colleague);
        }

        public T CreateColleague<T>() where T: Colleague, new() {
            var c = new T();
            c.SetMediator(this);
            this.colleagues.Add(c);
            return c;
        }
        public override void Send(string message, Colleague colleague)
        {
            /*if (colleague == this.colleague1){
                this.colleague2.HandleNotification(message);
            }
            else {
                this.colleague1.HandleNotification(message);
            }*/

            this.colleagues.Where(c => c != colleague).ToList().ForEach(c => c.HandleNotification(message));
        }
    }
}