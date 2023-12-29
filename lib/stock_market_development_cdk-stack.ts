import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as iam from 'aws-cdk-lib/aws-iam'
// import { CodePipeline, CodePipelineSource, ShellStep } from 'aws-cdk-lib/pipelines';
import { Construct } from 'constructs';
import path = require('path');
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class StockMarketDevelopmentCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    // In Block stage untill concurrent build request fullfill by AWS Team

    // new CodePipeline (this, 'Pipeline', {
    //   pipelineName: 'TestPipeline',
    //   synth: new ShellStep('Synth', {
    //     input: CodePipelineSource.gitHub ('harrymkwn/StockMarketDevelopmentCDK', 'main'),
    //     commands: ['npm ci',
    //                 'npm run build',
    //                 'npx cdk synth']
    //   }),
    // });


    const myRole = new iam.Role(this, 'My Role', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
    });
    const lambdaFunction = new lambda.Function(this, 'LambdaFunction', {
      runtime: lambda.Runtime.PYTHON_3_10, //using node for this, but can easily use python or other
      handler: 'index.handler',
      code: lambda.Code.fromAsset (path.join(__dirname, 'lambda')), //resolving to ./lambda directory
      role : myRole,
    });

    myRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));


    const listBucketsPolicy = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['s3:ListAllMyBuckets'],
      resources: ['arn:aws:s3:::*'],
    });

    // 👇 attach the policy to the function's role
    lambdaFunction.role?.attachInlinePolicy(
      new iam.Policy(this, 'list-buckets', {
        statements: [listBucketsPolicy],
      }),
    );
  }
}
