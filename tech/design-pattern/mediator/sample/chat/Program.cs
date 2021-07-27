using System;

namespace Chat
{
    class Program
    {
        static void Main(string[] args)
        {
            var teamChat = new TeamChatroom();

            var steve = new Developer("Steve");
            var justin = new Developer("Justing");
            var jenna = new Developer("Jenna");
            var kim = new Tester("Kim");
            var juila = new Tester("Julia");

            teamChat.RegisterMembers(steve, justin, jenna, kim, juila);

            Console.WriteLine();
            Console.WriteLine("-----------------");

            steve.Send("Hey everyone, we're going to be deploying at 2pm today");
            kim.Send("Ok, thanks for letting us know");

            Console.WriteLine();
            Console.WriteLine("-----------------");           

            steve.SendTo<Developer>("Make sure you execute unit tests before checking in");
        }
    }
}
