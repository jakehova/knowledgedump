using System;
using System.Collections.Generic;
using System.Linq;

namespace Chat
{
    // this is the mediator
    public class TeamChatroom : Chatroom
    {
        private List<TeamMember> teamMembers = new List<TeamMember>();

        public TeamChatroom() : base()
        {

        }

        public void RegisterMembers(params TeamMember[] teamMembers){
            foreach(var member in teamMembers){
                this.Register(member);
            }
        }

        public override void Register(TeamMember member)
        {
            member.SetChatroom(this);
            this.teamMembers.Add(member);
        }
        public override void Send(string from, string message)
        {
            this.teamMembers.ForEach(m => m.Receive(from, message));
        }

        public override void SendTo<T>(string from, string message)
        {
            this.teamMembers.OfType<T>().ToList().ForEach(m => m.Receive(from, message));
        }
    }
}
