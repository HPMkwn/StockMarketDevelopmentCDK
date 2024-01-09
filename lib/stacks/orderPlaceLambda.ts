import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import { Construct } from "constructs";
import * as path from 'path';

export class OrderPlaceLambdaStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
      super(scope, id, props);
        

      const lambdaFunction = new lambda.DockerImageFunction(this, 'DockerFunc', {
        code: lambda.DockerImageCode.fromImageAsset(path.join(__dirname, '../../assets/orderPlaceLambda/'),{
          exclude: ['cdk.out'],
          extraHash: "ap-south-1",
          assetName : 'stock-market-lambda',
        }),
        architecture: lambda.Architecture.ARM_64,
      });
  
      const api = new apigateway.LambdaRestApi(this, 'LambdaRestAPI',{
        handler : lambdaFunction,
        proxy : false
      })
  
      api.root.addResource('place-order').addMethod('POST',new apigateway.LambdaIntegration(lambdaFunction));
  
    }
}