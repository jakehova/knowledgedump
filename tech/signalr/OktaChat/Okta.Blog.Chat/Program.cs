using Microsoft.AspNetCore.Authentication.Cookies;
using Okta.AspNetCore;
using Okta.Blog.Chat.Hubs;

var builder = WebApplication.CreateBuilder(args);

/*
 var oktaMvcOptions = new OktaMvcOptions()
    {
        OktaDomain = Configuration["OktaSettings:OktaDomain"],
        ClientId = Configuration["OktaSettings:ClientId"],
        ClientSecret = Configuration["OktaSettings:ClientSecret"],
        Scope = new List<string> { "openid", "profile", "email" },
    };

builder.Services.AddAuthentication(options =>
    {
        options.DefaultAuthenticateScheme = CookieAuthenticationDefaults.AuthenticationScheme;
        options.DefaultSignInScheme = CookieAuthenticationDefaults.AuthenticationScheme;
        options.DefaultChallengeScheme = OktaDefaults.MvcAuthenticationScheme;
    })
    .AddCookie()
    .AddOktaMvc(oktaMvcOptions);*/

// Add services to the container.
builder.Services.AddRazorPages().AddRazorPagesOptions(options =>
    {
        //options.Conventions.AuthorizePage("/Chat");
    });

builder.Services.AddSignalR();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}
else
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.UseEndpoints(endpoints =>
{
    endpoints.MapRazorPages();
    endpoints.MapHub<ChatHub>("/chathub");
});

app.Run();
