using System;

namespace MediatorDemoSimple
{
    public class Colleague1 : Colleague
    {
        /*public Colleague1(Mediator mediator) : base(mediator)
        {

        }*/

        public override void Send(string message)
        {
            this.mediator.Send(message, this);
        }

        public override void HandleNotification(string message) {
            Console.WriteLine($"Colleague1 receives notification message: {message}");
        }

    }
}
