using System;

namespace MediatorDemoSimple
{
    public abstract class Colleague
    {
        protected Mediator mediator;

        /*public Colleague(Mediator mediator)
        {
            this.mediator = mediator;
        }*/

        internal void SetMediator(Mediator mediator){
            this.mediator = mediator;
        }

        public virtual void Send(string message)
        {
            this.mediator.Send(message, this);
        }

        public abstract void HandleNotification(string message);

    }
}
