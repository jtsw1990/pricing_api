# pricing_api
End to end pricing system for insurance pricing

## Overall design

![high_level_design](/assets/high_level_design.png)

## Components
- Product (Travel? since its alot simpler)
- Front end (Let's do kotlin for android?)
- REST API
- Pricing Engine (Placeholder statistical model)
- Back end webhosting service


### Front End


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
