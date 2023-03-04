# Maui

* App.xaml - defines app resources for the XAML layout.  
    * defaults are in **Resources** folder and define app wide colors and default styles.
* App.xaml.cs
    * constructor creates initial window and assigns it to MainPage property
        * MainPage property - determines which page is displayed when the application starts running 
        * This is where you override common platform-neutral app lifecycle events:
            * OnStart
            * OnResume
            * OnSleep
* AppShell.xaml - main structure of the .NET MAUI app
    * app styling, URI based navigation, layout options 
* MainPage.xaml - Contains user interface defintion



## XAML controls
* VerticalStackLayout - makes controls line up vertically
* ScrollView - (parent to vertical or horizatonal stack layout) adds scrollbar to view if there are too many items

## Backend 

