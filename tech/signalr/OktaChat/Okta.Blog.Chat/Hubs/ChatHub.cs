using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace Okta.Blog.Chat.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(string message)
        {
            //if (this.Context.User.Identity.IsAuthenticated)
            await Clients.All.SendAsync("ReceiveMessage", this.Context.User.Identity.Name, message);
        }
    }
}