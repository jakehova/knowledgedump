# .NET 

https://jasontaylor.dev/clean-architecture-getting-started/

## EF Core
**Best Practices**
* Only data layer should have a dependency on Entity Framework
* Keep DB Context class internal to the data layer project
    * Create an IServiceCollection extension method in the DataLayer that clients can use. The method should register the DbContext with the dependency injection framework.  The client should not know, or care, about persistence.
    * This ensures that client wont haver direct access to making database calls.  Also, other projects wont have an unnecessary dependency on EF Core
```
public static class AppContextService { 
    public static IServiceCollection AddAppContext (this IServiceCollection services, string connectionString) { 
        services.AddDbContext<AppContext>(options => { options.UseSqlServer(connectionString)});
        return services
    }
}
...
// In startup.ConfigureServices: 
services.AddAppContext(configuration.GetConnectionString("default"));
```
* Use Type Configuration instead of OnModelCreating for configuring domain models 
    * Use OnModelCreating to scan for types that perform entity configurations
    ```
    // in AppContext: DbContext class
    protected override void OnModelCreating(ModelBuilder modelBuiler) {
        modelBuiler.ApplyConfigurationsFromAssembly(assembly: typeof(AppContext).Assembly)
    }
    // in another file that is dedicated to configuration of different types 
    internal class AuthorConfig : IEntityTypeConfiguration<Author> {
        public void Configure(EntityTypeBuilder<Author> builder) {
            // model configuration using Fluent API
        }
    }
    ```
* Local Dev, Store Secrets using "dotnet user-secrets"
    * Might need to add Microsoft.Extensions.Configuration.UserSecrets package to project
    * Update appsettings.json with the property name and key/empty value pair: 
    ```
    // appsettings.json
    {
        "ConnectionStrings": {
            "default": ""
        }
    }
    ```
    * Go to root directory of your startup project and run "dotnet user-secrets init"
    * Set user secrets using: dotnet user-secrets set "ConnectionStrings:default" "<connection string>"
    * Production: Use key vault or environment variables for those secrets
* When configuring your database, create a specific user/pwd for the application so that it can be disabled for security.  never use SA creds
    * Ensure app user has least privelage
* Keep id fields private.  Then in the configuration IEntityTypeConfiguration file, let EF know about the id field: 
```
internal class AuthorConfig : IEntityTypeConfiguration<Author> {
    public void Configure(EntityTypeBuilder<Author> builder){
        builder.HasKey("id").HasName("PK_Authors");
    }
}
```
    * Instead of querying using IDs, use another property, or combination of properties, that is public but unique. 
* Generate IDs yourself.  Dont let third party software, i.e. the database, generate your domain IDs.
    * Let the domain model generate the ID itself (like assigning a GUID)
    * Use an ID factory and pass the generated ID to the model's constructor
* Avoid foreign key properties in the domain model
    * Use shadow properties (properties that are defined in FluentAPI rather than on the model itself) when EF can't generate a foreign key column
        * **Note** Shadow Properties should be used when the value/state of those properties are purely managed by the ChangeTracker (created/last updated/deleted/foreign key ids/etc)
* Ensure that all string fields are maxlength limited
    * [MaxLength(10)]
    * [Column(type = "varchar(10)")]
* Make collections read Only (IReadOnlyCollection<T> or IReadOnlyList<T>) and tell EF how to populate the private collection through configuration
```
public class Author {
    private readonly HashSet<Book> books;
    public IReadOnlyCollection<Book> Books => books;

    public Author(){
        books = new HashSet<Book>();
    }
}

// In confuration file
internal class AuthorConfig: IEntityTypeConfiguration<Author>{
    public void Configure(EntityTypeBuilder<Author> buidler) {
        builder.Metadata.FindNavigation(nameof(Author.Books))   // find the navigation property
                        .SetPropertyAccessMode(PropertyAccessMode.Field);   // tell ef to populate the field that has the same name (in this case the private field named "books")
    }
}
```
* Migrations
    * Create migrations for seed data
    * Use idempotent scripts to create/update the database (do not run migrations diretly against production)
        * Generate one script with all migrations that checks to see if a migration has been applied before applying it: dotnet ef migrations script -v -o ./scripts/idempotent.sql --idempotent
            * Use the script during deployment process 
            * Switches: 
                * -v   ← verbose console output
                * -o   ← path to where generated script file is placed
                * -i   ← makes the script idempotent
                * -s   ← Path to startup project (e.g. ASP.NET web app .csproj)
    * Managing Multiple DbContexts
        
    * **Notes**
        * Intro
            All commands must be executed from the root of the data layer project
        * Add new migration
            dotnet ef migrations add <MigrationName> -s ../Path/To/StartupProj<MigrationName>   ← name of the migration, without <>
        * Remove most recent migration
            dotnet ef migrations remove -s ../Path/To/StartupProj
        * Update local(!) database (this must only ever be used to update your own local database)
            dotnet ef database update -s ../Path/To/StartupProj

* Testing 
    * Use Moq to mock data

* Generic Repository Implementation for simple CRUD
```
public class GenericRepository<T> where T : class,   {
    internal DbContext _context;
    internal DbSet<T> _dbSet;

    public GenericRepository(DbContext context) {
        _context = context;
        _dbSet = context.Set<T>();
    }

    public IEnumerable<T> All(){
        return _dbSet.AsNoTracking().ToList();
    }

    public IEnumerable<T> FindBy(Expression<Func<T, bool>> predicate) {
        var results = _dbSet.AsNoTracking().Where(predicate).ToList();
        return results;
    }

    public T FindByKey(int id) {
        // makes the assumption that IEntity interface is defined with int Id {get;set;} as its implementation.
        return _dbSet.AsNoTracking().SingleOrDefault(e => e.Id == id);
        // OR
        // use simple Find which will search cache first before going to db
        return _dbSet.Find(id);
    }

    public IEnumerable<T> AllInclude (params Expression<Func<T, object>>[] includeProperties){
        return GetAllIncluding(includeProperties).ToList();
    }

    public IEnumerable<T> FindByInclude(Expression<Func<T, bool>> prediate, params Expression<Func<T, object>>[] includeProperties){
        var query = GetAllIncluding(includeProperties);
        IEnumerable<T> results = query.Where(predicate).ToList();
        return results;
    }

    private IQueryable<T> GetAllIncluding(params Expression<Func<T, object>>[] includeProperties) {
        IQueryable<T> queryable = _dbSet.AsNoTracking();

        return includeProperties.Aggregate(queryable, (current, includeProperty) => current.Include(includeProperty));
    }

    public voic Insert(T entity) {
        _dbSet.Add(entity);
    }

    public void Update(T entity) {
        _dbSet.Attach(entity);
        _context.Entry(entity).State = EntityState.Modified;
    }
}
```

