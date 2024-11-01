'''
You are designing a workflow in AWS Step Functions to process a dataset of product information. 
Each product record is an object with properties including id, name, and category. 
The input to your state machine is an array of these product records. 
Your task is to design a part of the state machine that accomplishes the following steps:

    Filter Products: Filter the array to include only products that belong to the category "Electronics".
    Format Product Names: For the filtered products, create a new array that contains strings formatted 
    as "ProductName (ProductID)", where ProductName is the name of the product and ProductID is its ID.
    Output Formation: The state machine should output this newly formatted array of string.

Given the current limitations of AWS Step Functions' intrinsic functions for direct array manipulations like filtering and mapping, 
describe how you would design this workflow. Assume you can use AWS Lambda if necessary, but try to minimize external calls. 
How would you leverage Step Functions' capabilities to implement this logic?

Follow-up Questions:

    How would you handle errors or exceptions in this workflow, for instance, if a product record is missing a category or name?
    If the input array is large, what considerations might you have regarding the performance and execution time of your 
    state machine?
    How would you modify your state machine if you later needed to include products 
    from both "Electronics" and "Books" categories?

This question tests your ability to design complex workflows using AWS Step Functions, 
including your understanding of its intrinsic functions, your creativity in working around its limitations 
for direct array manipulations, and your ability to integrate AWS Lambda for tasks that cannot be accomplished 
with Step Functions alone. It also explores error handling and performance considerations in state machine design.
'''
import json

def lambda_handler(event, context):
    # Create a new array that contains strings formatted as "ProductName (ProductID)"
    formatted_products = [f"{product['name']} ({product['id']})" for product in event]
    return formatted_products


def lambda_handler(event, context):
    # Filter the array to include only products that belong to the category "Electronics".
    filtered_products = [product for product in event if product.get('category') == 'Electronics']
    return filtered_products

{
  "Comment": "Product Processing State Machine",
  "StartAt": "Filter Products",
  "States": {
    "Filter Products": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:FilterProducts",
      "Next": "Format Product Names"
    },
    "Format Product Names": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:FormatProductNames",
      "End": True
    }
  }
}