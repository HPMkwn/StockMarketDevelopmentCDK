import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { OrderPlaceLambdaStack } from './stacks/orderPlaceLambda'; './stacks/OrderPlaceLambdaStack'


export class StockMarketDevelopmentCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
  }
}
