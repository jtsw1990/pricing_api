# pricing_api
End to end pricing system for insurance pricing
General framework that can be used as a base proof of concept for other projects
TODO: Add commercial pricing algorithm component. This goes in between response and technical model outputs.

## Overall design

![high_level_design](/assets/high_level_design.png)

## Components
- Product (Travel? since its alot simpler)
- Front end (Let's do kotlin for android?)
- REST API
- Pricing Engine (Placeholder statistical model)
- Back end webhosting service

### Products
Currently doing travel. Build should be done keeping in mind that extensibility is extremely important.
Interchangeable components:
- Contract
- Mapping table
- Technical Model
Classes should be written around these constraints


### Front End
Front end platform TBC
- Mobile (kotlin) based app
- Flask based web application

### REST API

Uses the Flask library and Api class with GET and POST class methods defined.
Current test build runs on `http://127.0.0.1:5000`

| URI           | Resource      | Description | Implemented |
| ------------- |:-------------:| -----------:| -----------:|
| /healthcheck | GET | Returns status of the server | Y |
| /pricing | GET | Returns the contract for the current pricing algorithm |
| /pricing | POST | Returns the price given a valid request body |


### Pricing Engine

Travel algorithm currently consists of a very simplified linear regression model.
This is to be replaced once structure is built.

### Server

## How to use
1. Download an API development tool. Testing and building was done using [POSTMAN](https://www.postman.com/downloads/)
TODO: Insert instructions for getting schemas and mappings
TODO: Contact digitcal ocean for backend hosting 
