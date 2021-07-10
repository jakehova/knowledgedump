FROM mcr.microsoft.com/dotnet/core/aspnet AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk AS build
WORKDIR /src
COPY ["dotnet-mvc.csproj", "./"]
RUN dotnet restore "./dotnet-mvc.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "dotnet-mvc.csproj" -c Release -o /app

FROM build as publish
RUN dotnet publish "dotnet-mvc.csproj" -c Release -o /app

FROM base as final
ENV ASPNETCORE_URLS="http://*:5000"
EXPOSE 5000
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT [ "dotnet", "dotnet-mvc.dll" ]