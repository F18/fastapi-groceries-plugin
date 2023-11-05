# FastAPI Grocery List

A simple FastAPI template for a web-based grocery list app.

Based on the VS Code FastAPI tutorial, this repository provides a basic template
for a simple FastAPI application. We will create a grocery list app using
FastAPI.

We will install `FastAPI` for creating the app, `uvicorn` to work as the server,
and `Redis` and `type-redis` for handling data storage and interacting with a
Redis database. The goal is to get familiar with these tools and also to
understand how to work with FastAPI in the Visual Studio Code terminal, editor,
and debugger.

## Pydantic Model

We can define our grocery list items by using Pydantic, a data validation and
parsing library that integrates seamlessly with FastAPI. Pydantic lets you
define data models using Python classes with type hints for automatic validation
and parsing of incoming data (called "payloads") in API requests.

Let's create a model for our grocery list items. We will use the ItemPayload
model to define the data structure of the items to add to the grocery list. This
model will have three fields: item_id, item_name, and quantity.