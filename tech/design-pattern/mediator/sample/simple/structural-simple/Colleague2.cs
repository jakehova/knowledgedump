using System;

namespace MediatorDemoSimple
{
    public class Colleague2 : Colleague
    {
        /*public Colleague2(Mediator mediator) : base(mediator)
        {

        }*/

        public override void Send(string message)
        {
            this.mediator.Send(message, this);
        }

        public override void HandleNotification(string message) {
            Console.WriteLine($"Colleague2 receives notification message: {message}");
        }

    }
}
