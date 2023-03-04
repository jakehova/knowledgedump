# build and publish the app
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS build
WORKDIR /src
## copy csproj and restore as distinct layers
COPY Okta.Blog.Chat.csproj ./
RUN dotnet restore
## copy everything else and publish app
COPY . ./
RUN dotnet publish -c release -o /app --no-restore

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
COPY --from=build /app ./
ENTRYPOINT ["dotnet", "Okta.Blog.Chat.dll"]