import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";


const api = new awsx.apigateway.API("hello-world", {
    routes: [{
        path: "/",
        method: "GET",
        eventHandler: async(event) => {
            return {
                statusCode: 200,
                body: "hello world"
            }
        }
    }]
})

export const apiurl = api.url