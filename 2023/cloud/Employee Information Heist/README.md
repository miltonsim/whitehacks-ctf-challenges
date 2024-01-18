## Employee Information Heist

### Description
Oliver, a new employee at your company, has implemented an Azure AD authentication system on the company website that he claims is very secure. 

As the HR manager, you've accidentally forgotten to input Oliver's job title into the HR system when he onboarded and don't want to ask him directly. Can you find a way to retrieve this information using the new authentication system? 

Remember, Oliver thinks that no one will be able to find out anything about the company through this system, so you'll need to be clever and resourceful in order to succeed.

Could you help us to find out his job title?

Do not pentest the website. You only need Google and might need a programming language.

### Steps 
1. **Retrieve Access Token** : Extract the access token from the company's website authenticated by Azure AD. 
2. **Use Microsoft Graph API** : Request user information via Microsoft Graph API using the access token.