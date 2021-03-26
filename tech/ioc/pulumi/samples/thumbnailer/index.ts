import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const image = awsx.ecr.buildAndPushImage("thumbnailer", {
    context: "./app",
});

// A bucket to store videos and thumbnails.
const bucket = new aws.s3.Bucket("thumbnailer", {
    forceDestroy: true,
    website: {
        indexDocument: "cat.jpg",
    }
});

const bucketPolicy = new aws.s3.BucketPolicy("thumbnailer", {
    bucket: bucket.id,
    policy: bucket.arn.apply(arn => JSON.stringify({
        "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    `${arn}/*`
                ]
            }]
    }))
})

const role = new aws.iam.Role("thumbnailerRole", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({ Service: "lambda.amazonaws.com" }),
});
const lambdaFullAccess =  new aws.iam.RolePolicyAttachment("lambdaFullAccess", {
    role: role.name,
    policyArn: aws.iam.ManagedPolicies.AWSLambdaFullAccess,
});

const thumbnailer = new aws.lambda.Function("thumbnailer", {
    packageType: "Image",
    imageUri: image.imageValue,
    role: role.arn,
    timeout: 900,
});

// When a new video is uploaded, run the FFMPEG task on the video file.
// Use the time index specified in the filename (e.g. cat_00-01.mp4 uses timestamp 00:01)
bucket.onObjectCreated("onNewVideo", thumbnailer, { filterSuffix: ".mp4" });

// When a new thumbnail is created, log a message.
bucket.onObjectCreated("onNewThumbnail", new aws.lambda.CallbackFunction<aws.s3.BucketEvent, void>("onNewThumbnail", {
    callback: async bucketArgs => {
        console.log("onNewThumbnail called");
        if (!bucketArgs.Records) {
            return;
        }

        for (const record of bucketArgs.Records) {
            console.log(`*** New thumbnail: file ${record.s3.object.key} was saved at ${record.eventTime}.`);
        }
    },
    policies: [
        aws.iam.ManagedPolicies.AWSLambdaFullAccess,                 // Provides wide access to "serverless" services (Dynamo, S3, etc.)
    ],
}), { filterSuffix: ".jpg" });

export const bucketName = bucket.id;
export const url = bucket.websiteEndpoint
