using System;

namespace Chat
{
    // this is the colleage
    public abstract class TeamMember
    {
        private Chatroom chatRoom;
        public string Name { get; set; }
        public TeamMember(string name)
        {
            this.Name = name;
        }

        internal void SetChatroom(Chatroom chatroom)
        {
            this.chatRoom = chatroom;
        }

        public void Send(string message)
        {
            this.chatRoom.Send(this.Name, message);
        }

        public void SendTo<T>(string message) where T : TeamMember
        {
            this.chatRoom.SendTo<T>(this.Name, message);
        }

        public virtual void Receive(string from, string message)
        {
            Console.WriteLine($"from { from}: '{message}'");
        }
    }
}
