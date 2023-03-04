# Certs

## Create Self Signed Cert
```
# clean existing certs if any
dotnet dev-certs https --clean
# create a new cert on macOS/Linux
dotnet dev-certs https -ep ${HOME}/.aspnet/https/aspnetapp.pfx -p mypass123
# create a new cert on Windows
dotnet dev-certs https -ep %USERPROFILE%\.aspnet\https\aspnetapp.pfx -p mypass123
# trust the cert
dotnet dev-certs https --trust
```