import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam'
import{ Construct } from 'constructs';
import { Function, InlineCode, Runtime, Code} from 'aws-cdk-lib/aws-lambda';
import* as path from 'path';


export class MyLambdaStack extends cdk.Stack {
    constructor (scope: Construct, id: string, stageName: string, props?: cdk.StackProps) {
      super (scope, id, props);

      const myRole = new iam.Role(this, 'My Role', {
        assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      });


      new Function(this, 'LambdaFunction', {
        runtime: Runtime.NODEJS_18_X, //using node for this, but can easily use python or other
        handler: 'handler.handler',
        code: Code.fromAsset (path.join(__dirname, 'lambda')), //resolving to ./lambda directory
        environment: { "stageName": stageName} //inputting stagename
      });


      myRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));
   // myRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaVPCAccessExecutionRole")); // only required if your function lives in a VPC
    }
}