<p align="center">
  <img src="extra/pysysair.png" width="300"/>
  <br>[<b>Py</b>thon <b>Sys</b>tem<b>air</b>]
</p>

#### Description

This software offers a streamlined Python interface for interacting with Systemair SAVE ventilation units through the Systemair Homesolutions Cloud Platform.

#### Technology
Built atop asyncio, the Python GraphQL Client leverages ariadne-codegen for schema introspection. This facilitates easy updates in response to API changes, a necessary feature given Systemair's limited public API documentation.


#### Authentication

The Systemair GraphQL API utilizes OIDC. Despite its advantages, it lacks user-friendly options for managing integrations, which restricts the OAuth2 Flows available. Nonetheless, it supports the password grant option, allowing users to exchange email-password credentials for tokens to interact with their GraphQL service.


#### Usage

To integrate `pysysair` into your project, ensure you are registered at https://homesolutions.systemair.com with your ventilation systems linked to your account. Also, your must update your password at https://sso.systemair.com/auth/realms/iot/login-actions/authenticate?client_id=account-console to enable OAuth2 password grant functionality.

See [Examples](/examples) to get started.


#### Status

WIP: Currently in early development, this project is not yet complete with all intended features.

#### Author

Robert W <1263192+rbw@users.noreply.github.com>
