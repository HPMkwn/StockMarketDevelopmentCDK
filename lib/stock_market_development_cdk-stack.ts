import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as iam from 'aws-cdk-lib/aws-iam'
import * as ecr from 'aws-cdk-lib/aws-ecr'
import * as dockerFunction from 'aws-cdk-lib/'
// import { CodePipeline, CodePipelineSource, ShellStep } from 'aws-cdk-lib/pipelines';
import { Construct } from 'constructs';
import path = require('path');
import { EcrImage } from 'aws-cdk-lib/aws-ecs';
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


    // const myRole = new iam.Role(this, 'My Role', {
    //   assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
    // });
    // myRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));
    
    // const ECRRole = new iam.Role(this, "ECRAccess Role", {
    //   assumedBy : new iam.ServicePrincipal('replication.ecr.amazonaws.com'),
    // })

    // ECRRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AmazonEC2ContainerRegistryPowerUser"));


    // const repo = new ecr.Repository(this, 'stock-market-lambda-demo',)



    // const lambdaFunction = new lambda.DockerImageFunction(this, 'DockerFunc', {
    //   code: lambda.DockerImageCode.fromImageAsset("./image"),
    //   memorySize : 1024,
    //   timeout : cdk.Duration.seconds(10),
    //   architecture : lambda.Architecture.ARM_64,
    //   role : ECRRole
    // });

    // const functionUrl = lambdaFunction.addFunctionUrl({
    //   authType: lambda. FunctionUrlAuthType. NONE,
    //   cors: { 
    //     allowedMethods: [lambda.HttpMethod. ALL],
    //     allowedHeaders: ["*"],
    //     allowedOrigins: ["*"],
    //   },
    // });

    // new cdk. CfnOutput(this, "FunctionUrlyalue", {
    //   value: functionUrl.url,
    // });

    const myLambda = new lambda.Function(this, 'MyLambdaFunction', {
      runtime: lambda.Runtime.PYTHON_3_10,
      handler: 'main.handler',
      code: lambda.Code.fromAsset("./image/src/"),  // Change this to the path of your Lambda function code
    });

    const myEcrRepository = ecr.Repository.fromRepositoryName(this, "MyEcrRepository", "stock-market-lambda");

    myEcrRepository.grantPull(myLambda);

  }
}
