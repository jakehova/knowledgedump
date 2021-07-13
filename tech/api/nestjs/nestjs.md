# NestJS

**Installation**
* npm i -g @nestjs/cli
* nest new <projectname>

| File | Purpose |
| --- | --- |
| app.controller.ts | a basic controller with a single route | 
| app.controller.spec.ts | The unit tests for the controller |
| app.module.ts | the root module of the application |
| app.service.ts | a basic service with a single method | 
| main.ts | *  the entry file for the application which uses the core function **NestFactory** to create a nest application instance. *  specifies listening port  |

**CLI**
* generate CRUD controller: nest g resource <resourcename>
* generate a controller: nest g controller <controller route>


**Components**
* NestFactory
  * exposes static methods that create an application
    * create<T>():
      *  returns application object.  That object implements INestApplication.
      *  T is optional but specifies HTTP framework to use: 
         *  Express: NestExpressApplication
         *  Fastify: NestFastifyApplication

* Controller
  * Handles requests and responses
  * Decorators tie required metadata to controller methods so that Nest can generate a routing map
  * Class Decorators
    * @Controller
      * parameters:
        * (1) optional string, names the path  
        * (1) optional JSON object:
          * JSON object can have a "host" option that would require the HTTP host of the incoming request matches a value: 
            * @Controller({host: 'admin.example.com'})
            * Can prefix the host value with ":" to denote dynamic and variable accessible value of the host making the call
              * ex: @Controller({host: ':account.example.com'}) => @Get getInfo(@HostParam('account') account: string){}
          * "scope" optional defines scope type
            * ex: @Controller({path:record, scope: Scope.REQUEST})
      * required to define a basic controller
  * Method Decorators
    * @Get || @Post || @Put || @Delete || @Patch || @Options || @Head || @All (handles all request types)
      * parameters:
        * (1) optional string 
          * If it has a special regex character: ?, +, *, () then:
            * will match any path that matches the regex
          * If it starts with ":" then:
            * defines expectation of having a parameter in the query string that can be directly accessed in the parameter list.
              * ex: @Get(':id') getRecord(@Params() params) => accessed in method body via params.id
              * ex: @Get(':id') getRecord(@Params('id') id:string) => accessed in method body via id parameter name
          * If it does not contain any special chars above, then it just defines the path on the route 
      * response: 
        * Standard Response Handling:
          * **Important**: objects and arrays are serialized to JSON. primitave types will NOT serialize to JSON.
          * Response is always 200 **EXCEPT** for Post which returns 201
        * LibrarySpecific Response Handling:
          * Can add the "@Res()" or "@Next", depending on framework (Express or Fastify) decorator on a parameter in the method's parameter list to denote overriden response handling.
            * In the method, you would use the parameter that is decorated like that respective framework handles responses. 
              * ex: @Get() findAll(@Res() response) { response.status(200).send();}
      * request:
        * @Req() decorator on parameter in parameter list holds the full request
        * @Body() decorator on parameter in parameter list holds the request body
        * @Query() decorator on parameter in parameter list holds the query string
    * @HttpCode
      * parameters: 
        *  (1) integer that relates to http status code to return 
           *  ex: @HttpCode(204)
    *  @Headers  
       *  parameters: 
          *  (1) string header key
          *  (2) string header value
          *  ex: @Header('Cache-Control', 'none')
    *  @Redirect
       *  parameters: 
          *  (1) optional string that gives url to redirect to
          *  (2) optional int (default 302) for http status code upon redirect
             *  the method being directed can return an JSON object with: {url:<string>, statusCode:<int>} to dynamically override the Redirect decorator on the method.


**Notes**
* Node Frameworks supported out of the box: 
  * Express: @nestjs/platform-express
  * Fastify 
  * **Note**: Works with any Node HTTP framework once an adapter is created
* [Uploading Files](https://docs.nestjs.com/techniques/file-upload)
  * Nest has a built in module based on multer middleware for Express
  * Install the types so you can access them: npm i -D @types/multer
* Scope
  * All resources are shared across incoming requests. 
    * Similar to .net core where you define things as transient, singleton, etc.  Provider types are
      * default (singleton) **Recommended**,
      * request (per request),
      * transient (per user session)
    * Used by using "scope" property
      * ex: @Injectable({scope:Scope.REQUEST})
      * ex: {provide:'CACHE_MANAGER', useClass: CacheManager, scope: Scope.TRANSIENT}