import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as iam from 'aws-cdk-lib/aws-iam'
import * as ecr from 'aws-cdk-lib/aws-ecr'
import * as events from '@aws-cdk/aws-events'
import * as targets from '@aws-cdk/aws-events-targets'
import * as dockerFunction from 'aws-cdk-lib/'
// import { CodePipeline, CodePipelineSource, ShellStep } from 'aws-cdk-lib/pipelines';
import { Construct } from 'constructs';
import path = require('path');
import { EcrImage } from 'aws-cdk-lib/aws-ecs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class StockMarketDevelopmentCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    ///////////////////////////////////////////////////// Deployment from CodePipeline ///////////////////////////////////////////////////

    // TODO: In Block stage untill concurrent build request fullfill by AWS Team

    // new CodePipeline (this, 'Pipeline', {
    //   pipelineName: 'TestPipeline',
    //   synth: new ShellStep('Synth', {
    //     input: CodePipelineSource.gitHub ('harrymkwn/StockMarketDevelopmentCDK', 'main'),
    //     commands: ['npm ci',
    //                 'npm run build',
    //                 'npx cdk synth']
    //   }),
    // });

    const myEcrRepository = ecr.Repository.fromRepositoryName(this, "MyEcrRepository", "stock-market-lambda");

    const lambdaFunction = new lambda.DockerImageFunction(this, 'DockerFunc', {
      code: lambda.DockerImageCode.fromImageAsset(path.join(__dirname, '../image/'),{
        exclude: ['cdk.out'],
        extraHash: "ap-south-1",
      }),
      architecture: lambda.Architecture.ARM_64,
    });
    myEcrRepository.grantPull(lambdaFunction);

    const functionUrl = lambdaFunction.addFunctionUrl({
      authType: lambda. FunctionUrlAuthType. NONE,
      cors: { 
        allowedMethods: [lambda.HttpMethod. ALL],
        allowedHeaders: ["*"],
        allowedOrigins: ["*"],
      },
    });

    new cdk.CfnOutput(this, "FunctionUrlyalue", {
      value: functionUrl.url,
    });


    ///////////////////////////////////////////////////// Deployment from Assets /////////////////////////////////////////////////////

    // const myLambda = new lambda.Function(this, 'MyLambdaFunction', {
    //   runtime: lambda.Runtime.PYTHON_3_10,
    //   handler: 'main.handler',
    //   code: lambda.Code.fromAsset("./image/src/"),  // Change this to the path of your Lambda function code
    // });

    // const myEcrRepository = ecr.Repository.fromRepositoryName(this, "MyEcrRepository", "stock-market-lambda");

    // myEcrRepository.grantPull(myLambda);

  }
}
