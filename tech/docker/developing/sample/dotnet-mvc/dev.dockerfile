FROM mcr.microsoft.com/dotnet/core/sdk

LABEL author="JAcob"

ENV ASPNETCORE_URLS=http://*:5000
ENV DOTNET_USE_POLLING_FILE_WATCHER=1
ENV ASPNETCORE_ENVIRONMENT=development

WORKDIR /app

ENTRYPOINT ["/bin/bash", "-c", "dotnet restore && dotnet watch run"]