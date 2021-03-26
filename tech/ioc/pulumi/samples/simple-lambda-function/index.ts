import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// allows aws access to the lambda environment in aws 
const role = new aws.iam.Role("my-function-role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "lambda.amazonaws.com"
    })
});

// create lambda function
//  note: the role.arn is an output from the previous role creation step.  it also signals to this 
//          lambda function to not start until that role creation step is complete
const lambdaFunction = new aws.lambda.Function("my-function", {
    role: role.arn,
    handler: "index.handler",
    runtime: aws.lambda.NodeJS12dXRuntime,
    code: new pulumi.asset.AssetArchive({
        "index.js": new pulumi.asset.StringAsset(
            "exports.handler = (e, c, cb) => cb(null, { statusCode: 200, body: 'Hello World'});",
        )
    })
})

export const functionName = lambdaFunction.name