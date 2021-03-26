# Socrata Query Language (SoQL)

* Used for queries and transformations
* https://dev.socrata.com/docs/transforms
* Column names are written
    * use underscores no spaces
    * use backticks no quotes
* Use double or single quotes to delimit strings
* "error" is a reserved method name that takes in a string.  you can include column value by using concatination symbol "||" to substitute string interpretation
    *  ex:  error("unknown value: " || `age` || " years old")
*  Datetime Formats
      *  ex: 
        ``` case(
                date_extract_y(
                    coalesce(
                        forgive(
                            to_floating_timestamp(`date`, '%Y-%m-%dT%H:%M:%S.%f')
                        ),
                        forgive(
                            to_floating_timestamp(`date`, '%Y%m%d')
                        ),
                        forgive(
                            to_floating_timestamp(`date`, '%m%d%Y')
                        ),
                        forgive(
                            to_floating_timestamp(`date`, '%Y%m%d')
                        ),
                        forgive(
                            to_floating_timestamp(`date`, '%Y%d%m')
                        )
                    )
                ) 
                >= 2018,  
                coalesce(
                    forgive(
                        to_floating_timestamp(`date`, '%Y-%m-%dT%H:%M:%S.%f')
                    ),
                    forgive(
                        to_floating_timestamp(`date`, '%Y%m%d')
                    ),
                    forgive(
                        to_floating_timestamp(`date`, '%m%d%Y')
                    ),
                    forgive(
                        to_floating_timestamp(`date`, '%Y%m%d')
                    ),
                    forgive(
                        to_floating_timestamp(`date`, '%Y%d%m')
                    )
                ),
                true, 
                error(`date`)
            )
        ```