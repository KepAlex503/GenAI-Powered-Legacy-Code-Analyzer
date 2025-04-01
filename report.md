# 📘 Extracted Business Requirements

## 🔹 `run_install`
**Location**: `..\EeazyCRM\eeazycrm\__init__.py:24`

**Description**:
The `run_install` method is likely used to initiate the installation process of an application within the EeazyCRM system. It is unclear who calls this method without additional context.

---

## 🔹 `create_app`
**Location**: `..\EeazyCRM\eeazycrm\__init__.py:30`

**Description**:
The `create_app` method is used to initialize and configure an application instance with a specific configuration class. It is likely called during the startup of the EeazyCRM application.

---

## 🔹 `run_migrations_offline`
**Location**: `..\EeazyCRM\migrations\env.py:36`

**Description**:
The `run_migrations_offline` method is likely used to execute database migrations when the application is not connected to the internet or the database server. It's unclear who calls this method without more context, but it could be called by a system administrator or automatically by the system during startup or maintenance periods.

---

## 🔹 `run_migrations_online`
**Location**: `..\EeazyCRM\migrations\env.py:57`

**Description**:
The `run_migrations_online` method is likely used to execute online database migrations in the EeazyCRM application. It's not specified who calls this method, but it's likely called by system administrators or automatically during system updates.

---

## 🔹 `process_revision_directives`
**Location**: `..\EeazyCRM\migrations\env.py:68`

**Description**:
The `process_revision_directives` method is likely used to handle or process directives related to revisions in the context of a migration environment in the EeazyCRM application. It is unclear who calls this method based on the provided information.

---

## 🔹 `app`
**Location**: `..\EeazyCRM\tests\conftest.py:8`

**Description**:
The `app` method is used in testing to create an instance of the application under test. It is likely called by test cases or test suites within the EeazyCRM project.

---

## 🔹 `client`
**Location**: `..\EeazyCRM\tests\conftest.py:17`

**Description**:
The `client` method is likely used in the context of testing in the EeazyCRM application. It doesn't belong to any class and doesn't return anything, suggesting it might be setting up or manipulating a client object for testing purposes. It is called by the testing framework or other testing methods in the application.

---

## 🔹 `runner`
**Location**: `..\EeazyCRM\tests\conftest.py:22`

**Description**:
The `runner` method is likely used in the context of testing in the EeazyCRM application, possibly to initiate or run a specific test scenario. It is probably called by various test cases or scripts within the test suite.

---

## 🔹 `auth`
**Location**: `..\EeazyCRM\tests\conftest.py:27`

**Description**:
The `auth` method is likely used for handling authentication of a 'client' in the EeazyCRM application. It is probably called when a client tries to access certain features or areas of the application that require authentication.

---

## 🔹 `account`
**Location**: `..\EeazyCRM\tests\conftest.py:32`

**Description**:
The `account` method in the context of EeazyCRM tests doesn't belong to any class and doesn't return anything. It seems to be used for setting up or configuring client account related settings or data for testing purposes. It's likely called within the testing framework.

---

## 🔹 `test_new_account_validate_input`
**Location**: `..\EeazyCRM\tests\test_accounts.py:11`

**Description**:
The `test_new_account_validate_input` method is used for testing the input validation of a new account in the EeazyCRM system. It is likely called by a testing framework to ensure that the account creation process correctly handles and validates user input.

---

## 🔹 `test_new_account`
**Location**: `..\EeazyCRM\tests\test_accounts.py:19`

**Description**:
The `test_new_account` method is used to test the functionality of creating a new account in the EeazyCRM system. It is likely called by a testing framework to ensure that the account creation process works correctly when a client is logged in.

---

## 🔹 `test_login`
**Location**: `..\EeazyCRM\tests\test_auth.py:6`

**Description**:
The `test_login` method is used to test the login functionality of the application. It is likely called by a testing framework or a test runner in the EeazyCRM project.

---

## 🔹 `test_new_user`
**Location**: `..\EeazyCRM\tests\test_auth.py:18`

**Description**:
The `test_new_user` method is used for testing the user authentication process in the EeazyCRM application. It is likely called by a testing framework to ensure that the login, new user registration, and logout functionalities are working correctly.

---

## 🔹 `test_remove_user`
**Location**: `..\EeazyCRM\tests\test_auth.py:32`

**Description**:
The `test_remove_user` method is used to test the functionality of removing a user from the system. It is called within the test suite of the EeazyCRM application.

---

## 🔹 `test_login_validate_input`
**Location**: `..\EeazyCRM\tests\test_auth.py:42`

**Description**:
The `test_login_validate_input` method is used to test the validation of user input during the login process in the EeazyCRM application. It is likely called by a testing framework to ensure the 'AuthActions.login' function works correctly.

---

## 🔹 `test_new_user_validate_input`
**Location**: `..\EeazyCRM\tests\test_auth.py:54`

**Description**:
The method `test_new_user_validate_input` is used for testing the input validation of a new user in the authentication process. It is likely called by a testing framework or test runner in the context of automated testing for the EeazyCRM application.

---

## 🔹 `AccountActions.__init__`
**Location**: `..\EeazyCRM\tests\actions\accounts.py:2`

**Description**:
The `AccountActions.__init__` method is the initializer or constructor for the `AccountActions` class in the EeazyCRM application. It is automatically called when an instance of the `AccountActions` class is created, taking 'client' as an argument.

---

## 🔹 `AccountActions.new_account`
**Location**: `..\EeazyCRM\tests\actions\accounts.py:5`

**Description**:
The `AccountActions.new_account` method in the `AccountActions` class is used to create a new account using the provided parameters (`acc_params`). It is likely called by other methods or functions that need to create a new account in the EeazyCRM system.

---

## 🔹 `AuthActions.__init__`
**Location**: `..\EeazyCRM\tests\actions\auth.py:2`

**Description**:
The `AuthActions.__init__` method is the initializer or constructor for the `AuthActions` class in the EeazyCRM application, which is likely used to handle authentication actions. It is called when an instance of the `AuthActions` class is created, taking a 'client' as an argument.

---

## 🔹 `AuthActions.login`
**Location**: `..\EeazyCRM\tests\actions\auth.py:5`

**Description**:
The `AuthActions.login` method in the `AuthActions` class is used to handle the login functionality, taking an 'email' and 'password' as arguments. It is likely called by the user interface or other parts of the application where user authentication is required.

---

## 🔹 `AuthActions.new_user`
**Location**: `..\EeazyCRM\tests\actions\auth.py:11`

**Description**:
The `AuthActions.new_user` method in the `AuthActions` class is used to create a new user with the provided 'last_name' and 'email'. It is likely called by the authentication system or user registration process in the EeazyCRM application.

---

## 🔹 `AuthActions.remove_user`
**Location**: `..\EeazyCRM\tests\actions\auth.py:18`

**Description**:
The `AuthActions.remove_user` method in the `AuthActions` class is used to remove a user from the authentication system using their email. It is likely called by an administrator or a function handling user management in the EeazyCRM application.

---

## 🔹 `AuthActions.logout`
**Location**: `..\EeazyCRM\tests\actions\auth.py:24`

**Description**:
The `AuthActions.logout` method in the `AuthActions` class is used to handle the logout process for a user in the EeazyCRM application. This method is likely called when a user chooses to log out of the application.

---

## 🔹 `upgrade`
**Location**: `..\EeazyCRM\migrations\versions\56a0ecfd603a_.py:19`

**Description**:
The `upgrade` method is likely used in the context of database migrations in the EeazyCRM application. It is probably called by a migration tool or script to apply changes to the database schema or data.

---

## 🔹 `downgrade`
**Location**: `..\EeazyCRM\migrations\versions\56a0ecfd603a_.py:29`

**Description**:
The `downgrade` method is likely used in the context of database migrations in the EeazyCRM application, where it's responsible for reverting the database to a previous state. It is typically called by the migration management system when a downgrade in the database version is required.

---

## 🔹 `filter_accounts_adv_filters_query`
**Location**: `..\EeazyCRM\eeazycrm\accounts\forms.py:28`

**Description**:
The method `filter_accounts_adv_filters_query` likely applies advanced filters to a query related to accounts in the EeazyCRM software. It is unclear who calls this method based on the provided context.

---

## 🔹 `Account.account_list_query`
**Location**: `..\EeazyCRM\eeazycrm\accounts\models.py:37`

**Description**:
The `Account.account_list_query` method in the `Account` class is likely used to query a list of accounts in the EeazyCRM system. It's probably called by other methods or functions that need to retrieve account information.

---

## 🔹 `Account.get_label`
**Location**: `..\EeazyCRM\eeazycrm\accounts\models.py:44`

**Description**:
The `Account.get_label` method in the `Account` class is likely used to retrieve the label of a specific account. It is called by any function or method that needs to display or use the label of an account in the EeazyCRM application.

---

## 🔹 `Account.get_account`
**Location**: `..\EeazyCRM\eeazycrm\accounts\models.py:48`

**Description**:
The `Account.get_account` method in the `Account` class is used to retrieve the details of a specific account using its 'account_id'. It is likely called by other methods or functions that require account information in the EeazyCRM application.

---

## 🔹 `Account.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\accounts\models.py:51`

**Description**:
The `Account.__repr__` method in the `Account` class is used to provide a string representation of the Account object. It is automatically called by Python when we try to print the object or when we use it in a string context.

---

## 🔹 `set_filters`
**Location**: `..\EeazyCRM\eeazycrm\leads\filters.py:9`

**Description**:
The `set_filters` method is likely used to establish or update filters for leads in the EeazyCRM system, based on a given filter ID ('f_id'). It is probably called by other methods or functions that need to apply specific filters to the leads data.

---

## 🔹 `set_date_filters`
**Location**: `..\EeazyCRM\eeazycrm\leads\filters.py:36`

**Description**:
The `set_date_filters` method is used to apply date filters to various types of data such as accounts, contacts, deals, and leads in the EeazyCRM system. It is likely called by other methods or functions that require filtered data based on specific date ranges.

---

## 🔹 `reset_accounts_filters`
**Location**: `..\EeazyCRM\eeazycrm\accounts\routes.py:50`

**Description**:
The `reset_accounts_filters` method is likely used to clear or reset any filters applied to the accounts in the EeazyCRM application. It's not specified who calls this method, but it could be called by any part of the application that needs to clear account filters, such as a user interface or another method.

---

## 🔹 `get_accounts_view`
**Location**: `..\EeazyCRM\eeazycrm\accounts\routes.py:64`

**Description**:
The `get_accounts_view` method is used to retrieve a view of accounts, applying common filters such as search, owner, and date filters, and checking access permissions. It is likely called by a controller or handler in the application when an accounts view is requested.

---

## 🔹 `update_account`
**Location**: `..\EeazyCRM\eeazycrm\accounts\routes.py:91`

**Description**:
The `update_account` method is likely called by a component in the EeazyCRM system to update the details of a specific account, identified by 'account_id'. It retrieves the account using 'Account.get_account' and checks the access permissions using 'check_access' before making any changes.

---

## 🔹 `get_account_view`
**Location**: `..\EeazyCRM\eeazycrm\accounts\routes.py:135`

**Description**:
The `get_account_view` method is likely used to retrieve the view or details of a specific account, identified by 'account_id'. It is probably called by various parts of the EeazyCRM system where account details need to be displayed, and it also checks if the user has access to view the account.

---

## 🔹 `new_account`
**Location**: `..\EeazyCRM\eeazycrm\accounts\routes.py:143`

**Description**:
The `new_account` method is likely used to create a new account in the EeazyCRM system. It is probably called by a user or system process, and it uses the `check_access` method to verify permissions before proceeding with the account creation.

---

## 🔹 `delete_account`
**Location**: `..\EeazyCRM\eeazycrm\accounts\routes.py:177`

**Description**:
The `delete_account` method is used to delete a specific account from the system using the provided 'account_id'. It is likely called by an administrator or a user with sufficient privileges, after checking access permissions with the 'check_access' method.

---

## 🔹 `reset_filters`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:250`

**Description**:
The `reset_filters` method is used to reset all filters applied to accounts, contacts, deals, and leads in the EeazyCRM system. It is likely called by a user or system process when a clear or reset action is required on the CRM filters.

---

## 🔹 `CommonFilters.set_owner`
**Location**: `..\EeazyCRM\eeazycrm\common\filters.py:12`

**Description**:
The `CommonFilters.set_owner` method in the `CommonFilters` class is used to set or update the owner of a specific filter in the EeazyCRM application. It is likely called by other methods or classes within the application that need to change the ownership of a filter.

---

## 🔹 `CommonFilters.set_accounts`
**Location**: `..\EeazyCRM\eeazycrm\common\filters.py:36`

**Description**:
The `CommonFilters.set_accounts` method in the `CommonFilters` class is used to set or update the account filters in a specific module with a given key. It is likely called by other methods or classes within the EeazyCRM application that need to apply or modify account filters.

---

## 🔹 `CommonFilters.set_contacts`
**Location**: `..\EeazyCRM\eeazycrm\common\filters.py:54`

**Description**:
The `CommonFilters.set_contacts` method in the `CommonFilters` class is used to set or update the contact filters in the EeazyCRM application. It is likely called by other methods or classes within the application that need to apply or modify contact filters.

---

## 🔹 `CommonFilters.set_search`
**Location**: `..\EeazyCRM\eeazycrm\common\filters.py:72`

**Description**:
The `CommonFilters.set_search` method in the `CommonFilters` class is used to set or update the search parameters for a given key in the filters. It is likely called by other methods or classes within the EeazyCRM application that require to filter or search through data.

---

## 🔹 `Paginate.__init__`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:6`

**Description**:
The `Paginate.__init__` method is the initializer for the Paginate class in the EeazyCRM application, which is used to set up pagination for a given query, specifying the page number and the number of results per page. It is called when an instance of the Paginate class is created.

---

## 🔹 `Paginate.items`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:24`

**Description**:
The `Paginate.items` method in the `Paginate` class is likely used to divide data into smaller, manageable chunks or pages. It is probably called by other methods or classes in the EeazyCRM application that need to display or process large amounts of data in a paginated format.

---

## 🔹 `Paginate.has_next`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:29`

**Description**:
The `Paginate.has_next` method in the `Paginate` class is used to check if there are more items or pages to be displayed in the pagination process. It is likely called by the system or user interface when handling paginated data in the EeazyCRM application.

---

## 🔹 `Paginate.has_prev`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:34`

**Description**:
The `Paginate.has_prev` method in the `Paginate` class is used to check if there is a previous page available in the pagination sequence. It is called by any function or method that needs to navigate through pages in the EeazyCRM application.

---

## 🔹 `Paginate.next_num`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:39`

**Description**:
The `Paginate.next_num` method in the `Paginate` class is likely used to determine the next page number in a pagination system. It is probably called by other methods or classes that handle page navigation in the EeazyCRM application.

---

## 🔹 `Paginate.prev_num`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:46`

**Description**:
The `Paginate.prev_num` method in the `Paginate` class is likely used to get the number of the previous page in a pagination system. It is called by any function or method that needs to navigate to the previous page in the pagination.

---

## 🔹 `Paginate.iter_pages`
**Location**: `..\EeazyCRM\eeazycrm\common\paginate.py:52`

**Description**:
The `Paginate.iter_pages` method in the `Paginate` class is likely used to iterate over pages in a paginated list or result set, with parameters to define the edges and current pages on both sides. The method is called by any part of the EeazyCRM application that requires pagination functionality.

---

## 🔹 `filter_contacts_adv_filters_query`
**Location**: `..\EeazyCRM\eeazycrm\contacts\forms.py:35`

**Description**:
The method `filter_contacts_adv_filters_query` is likely used to filter contacts based on some advanced query parameters in the EeazyCRM application. It's not clear who calls this method without additional context.

---

## 🔹 `Contact.contact_list_query`
**Location**: `..\EeazyCRM\eeazycrm\contacts\models.py:32`

**Description**:
The `Contact.contact_list_query` method in the `Contact` class is likely used to retrieve a list of contacts from a database or similar data source. It is probably called by other methods or functions that need to display or manipulate a list of contacts in the EeazyCRM application.

---

## 🔹 `Contact.get_label`
**Location**: `..\EeazyCRM\eeazycrm\contacts\models.py:44`

**Description**:
The `Contact.get_label` method in the `Contact` class is likely used to retrieve the label associated with a specific contact in the EeazyCRM system. It is called by any function or method that requires the label information of a contact.

---

## 🔹 `Contact.get_contact`
**Location**: `..\EeazyCRM\eeazycrm\contacts\models.py:48`

**Description**:
The `Contact.get_contact` method in the `Contact` class is used to retrieve a specific contact using the provided 'contact_id'. It is likely called by other methods or functions that require information about a specific contact in the EeazyCRM application.

---

## 🔹 `Contact.get_contact_name`
**Location**: `..\EeazyCRM\eeazycrm\contacts\models.py:51`

**Description**:
The `Contact.get_contact_name` method in the `Contact` class is likely used to retrieve the name of a specific contact. It is probably called by other methods or classes that need to display or use the contact's name in the EeazyCRM application.

---

## 🔹 `Contact.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\contacts\models.py:57`

**Description**:
The `Contact.__repr__` method in the `Contact` class is used to provide a string representation of the Contact object. This method is called internally by Python when it needs to represent the object in a string format, such as when printing.

---

## 🔹 `reset_contacts_filters`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:49`

**Description**:
The `reset_contacts_filters` method is used to clear or reset any filters applied to the contacts in the EeazyCRM application. It is likely called by the system or user when they want to view all contacts without any filters.

---

## 🔹 `get_contacts_view`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:63`

**Description**:
The `get_contacts_view` method is used to retrieve a view of contacts in the EeazyCRM application, applying various filters such as search, owner, accounts, and date filters, and checking access permissions. It is likely called by a controller or a route handler in the application when a user requests to view contacts.

---

## 🔹 `get_account_contacts`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:93`

**Description**:
The `get_account_contacts` method is used to retrieve the contacts associated with a specific account, identified by 'account_id'. It is likely called by other methods or functions within the EeazyCRM application that require information about an account's contacts.

---

## 🔹 `new_contact`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:109`

**Description**:
The `new_contact` method is likely called by a user interface in the EeazyCRM application to create a new contact, which involves uploading an avatar and checking access permissions.

---

## 🔹 `update_contact`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:150`

**Description**:
The `update_contact` method is used to update the details of a specific contact in the EeazyCRM system, identified by 'contact_id'. It is likely called by other methods or functions within the CRM system that need to modify contact information, after checking the access permissions.

---

## 🔹 `get_contact_view`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:198`

**Description**:
The `get_contact_view` method is likely called by a part of the CRM system to retrieve the view or information related to a specific contact, identified by 'contact_id'. It also checks if the user has the necessary access permissions before retrieving the contact information.

---

## 🔹 `delete_contact`
**Location**: `..\EeazyCRM\eeazycrm\contacts\routes.py:206`

**Description**:
The `delete_contact` method is used to delete a specific contact from the system using the provided 'contact_id'. It is likely called by a user or system process with sufficient access rights, as it checks access before proceeding with the deletion.

---

## 🔹 `set_p_filters`
**Location**: `..\EeazyCRM\eeazycrm\deals\filters.py:41`

**Description**:
The `set_p_filters` method is likely used to set or update filter parameters for a specific filter identified by 'f_id' in the EeazyCRM's deals module. It is called by any function or method that needs to modify the parameters of a filter in the CRM system.

---

## 🔹 `set_price_filters`
**Location**: `..\EeazyCRM\eeazycrm\deals\filters.py:73`

**Description**:
The `set_price_filters` method is used to apply specific price filters to a set of deals in the EeazyCRM system. It is likely called by other methods or classes within the system that need to filter deals based on price criteria.

---

## 🔹 `set_deal_stage_filters`
**Location**: `..\EeazyCRM\eeazycrm\deals\filters.py:88`

**Description**:
The `set_deal_stage_filters` method is used to set or update the filters for deal stages in the EeazyCRM system. It is likely called by other methods or functions that need to refine or change the criteria for displaying or processing deal stages.

---

## 🔹 `filter_deals_adv_filters_query`
**Location**: `..\EeazyCRM\eeazycrm\deals\forms.py:34`

**Description**:
The method `filter_deals_adv_filters_query` likely serves to filter deals based on advanced filters in the EeazyCRM system. It's unclear who calls this method without additional context.

---

## 🔹 `filter_deals_price_query`
**Location**: `..\EeazyCRM\eeazycrm\deals\forms.py:48`

**Description**:
The `filter_deals_price_query` method is likely used to filter deals based on their price in the EeazyCRM application. It's unclear who calls this method without additional context.

---

## 🔹 `DealStage.deal_stage_list_query`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:17`

**Description**:
The `DealStage.deal_stage_list_query` method in the `DealStage` class seems to be used for querying a list of deal stages in the EeazyCRM system. The specific caller of this method is not provided in the context.

---

## 🔹 `DealStage.get_label`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:21`

**Description**:
The `DealStage.get_label` method in the `DealStage` class is likely used to retrieve the label of a specific deal stage in a CRM system. It's probably called by other methods or classes that need to display or use the label of a deal stage.

---

## 🔹 `DealStage.get_deal_stage`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:25`

**Description**:
The `DealStage.get_deal_stage` method in the `DealStage` class is used to retrieve the stage of a deal based on the provided `deal_stage_id`. It is likely called by other methods or classes within the EeazyCRM application that need to know the current stage of a specific deal.

---

## 🔹 `DealStage.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:28`

**Description**:
The `DealStage.__repr__` method in the `DealStage` class is likely used to provide a human-readable representation of an instance of the class. It is called internally by Python when you try to print an instance of the `DealStage` class or when it is converted to a string.

---

## 🔹 `Deal.is_expired`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:47`

**Description**:
The `Deal.is_expired` method in the `Deal` class checks if a particular deal has expired. It is likely called by other methods or functions that need to determine the status of a deal within the EeazyCRM application.

---

## 🔹 `Deal.get_deal`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:54`

**Description**:
The `Deal.get_deal` method in the `Deal` class is used to retrieve a specific deal using its `deal_id`. It is likely called by other methods or functions that need to access or manipulate information about a specific deal in the EeazyCRM system.

---

## 🔹 `Deal.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\deals\models.py:57`

**Description**:
The `Deal.__repr__` method in the `Deal` class is used to provide a string representation of the `Deal` object. It is automatically called by Python when we try to print the object or when we use it in a string context.

---

## 🔹 `reset_deal_filters`
**Location**: `..\EeazyCRM\eeazycrm\deals\routes.py:21`

**Description**:
The `reset_deal_filters` method is used to clear or reset any applied filters on the deals in the EeazyCRM application. It is likely called by the system or user when they want to view all deals without any filters.

---

## 🔹 `get_deals_view`
**Location**: `..\EeazyCRM\eeazycrm\deals\routes.py:41`

**Description**:
The `get_deals_view` method is used to retrieve and filter deal-related data based on various parameters such as search, owner, accounts, contacts, date, price, and deal stage. It also checks for access permissions. It is likely called by a controller or a route handler in the EeazyCRM application to display the filtered deals data to the user.

---

## 🔹 `get_deal_view`
**Location**: `..\EeazyCRM\eeazycrm\deals\routes.py:77`

**Description**:
The `get_deal_view` method is used to retrieve the view of a specific deal identified by 'deal_id'. It is likely called by a function or method that requires information or details about a specific deal, after checking access permissions.

---

## 🔹 `new_deal`
**Location**: `..\EeazyCRM\eeazycrm\deals\routes.py:86`

**Description**:
The `new_deal` method is likely used to create a new deal in the EeazyCRM system. It is probably called by a user or system process, and it checks access permissions and retrieves account information before proceeding.

---

## 🔹 `update_deal`
**Location**: `..\EeazyCRM\eeazycrm\deals\routes.py:124`

**Description**:
The `update_deal` method is used to update the details of a specific deal in the EeazyCRM system, identified by its 'deal_id'. This method is likely called by a user or system process when changes need to be made to a deal's information.

---

## 🔹 `update_deal_stage_ajax`
**Location**: `..\EeazyCRM\eeazycrm\deals\routes.py:171`

**Description**:
The `update_deal_stage_ajax` method is used to update the stage of a specific deal in a CRM system, identified by 'deal_id', to a new stage, identified by 'stage_id'. It is likely called by an AJAX request from the front-end when a user changes the stage of a deal.

---

## 🔹 `User.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:45`

**Description**:
The `User.__repr__` method in the User class is used to provide a string representation of the User object. It is automatically called by Python when a string representation of the object is needed, such as when printing the object.

---

## 🔹 `sys_info`
**Location**: `..\EeazyCRM\eeazycrm\install\routes.py:24`

**Description**:
The `sys_info` method is likely used to retrieve and display system information in the EeazyCRM application. It's unclear who calls this method without additional context.

---

## 🔹 `setup_sys_user`
**Location**: `..\EeazyCRM\eeazycrm\install\routes.py:42`

**Description**:
The `setup_sys_user` method is likely used during the installation process of the EeazyCRM software to establish a system user. It's probably called by the installation script or process.

---

## 🔹 `ex_settings`
**Location**: `..\EeazyCRM\eeazycrm\install\routes.py:62`

**Description**:
The `ex_settings` method is likely used in the EeazyCRM application to extract settings related to currency and time zone. It is probably called when these settings need to be retrieved or displayed.

---

## 🔹 `empty_setup`
**Location**: `..\EeazyCRM\eeazycrm\install\routes.py:82`

**Description**:
The `empty_setup` method appears to be a placeholder or initial setup method in the EeazyCRM application, possibly used during the installation process. It's not clear who calls this method without additional context.

---

## 🔹 `finish`
**Location**: `..\EeazyCRM\eeazycrm\install\routes.py:154`

**Description**:
The `finish` method is likely used to conclude a certain process in the EeazyCRM application, possibly related to installation or setup, as it calls the `empty_setup` method. It is unclear who calls this method based on the provided context.

---

## 🔹 `page_not_found`
**Location**: `..\EeazyCRM\eeazycrm\main\routes.py:31`

**Description**:
The `page_not_found` method is likely used to handle 404 errors when a user tries to access a page that does not exist in the EeazyCRM application. It is probably called by the application's routing system when a requested route is not found.

---

## 🔹 `assign_filter`
**Location**: `..\EeazyCRM\eeazycrm\leads\filters.py:25`

**Description**:
The `assign_filter` method is used to assign a specific filter, identified by a key, to a filter object in the EeazyCRM application. It is likely called by other methods or classes within the application that need to apply specific filters to lead data.

---

## 🔹 `set_source`
**Location**: `..\EeazyCRM\eeazycrm\leads\filters.py:53`

**Description**:
The `set_source` method in the `EeazyCRM` application is likely used to set or update the source of leads based on certain filters and a key. It's probably called by other methods within the leads management module of the CRM when there is a need to update the source information of leads.

---

## 🔹 `set_status`
**Location**: `..\EeazyCRM\eeazycrm\leads\filters.py:69`

**Description**:
The `set_status` method in the `EeazyCRM` application is likely used to update or set the status of a lead based on certain filters and a key. This method is probably called by other methods or functions within the CRM application that handle lead management.

---

## 🔹 `lead_source_query`
**Location**: `..\EeazyCRM\eeazycrm\leads\forms.py:16`

**Description**:
The method `lead_source_query` does not have a clear business functionality or purpose based on the provided context. It appears to be a part of the EeazyCRM system, possibly related to querying the source of leads, but no specific details are given. The caller of this method is not specified in the context.

---

## 🔹 `filter_leads_adv_filters_admin_query`
**Location**: `..\EeazyCRM\eeazycrm\leads\forms.py:45`

**Description**:
The `filter_leads_adv_filters_admin_query` method is likely used to apply advanced filters to a query related to leads in the EeazyCRM system. It is probably called by an admin user or a system process that needs to filter leads based on certain criteria.

---

## 🔹 `filter_leads_adv_filters_user_query`
**Location**: `..\EeazyCRM\eeazycrm\leads\forms.py:55`

**Description**:
The method `filter_leads_adv_filters_user_query` likely filters user queries based on advanced filters for leads in the EeazyCRM system. The specific caller of this method is not provided in the context.

---

## 🔹 `LeadStatus.lead_status_query`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:11`

**Description**:
The method `LeadStatus.lead_status_query` in the `LeadStatus` class doesn't provide enough context to determine its exact purpose. However, given its name and location in a CRM system, it likely queries the status of leads in the system. The caller of this method could be any other method or function that requires information about the status of leads.

---

## 🔹 `LeadStatus.get_by_id`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:15`

**Description**:
The `LeadStatus.get_by_id` method in the `LeadStatus` class is used to retrieve the status of a lead in the CRM system using its unique identifier `lead_status_id`. It is likely called by other methods or classes that need to fetch or display the status of a specific lead.

---

## 🔹 `LeadStatus.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:18`

**Description**:
The `LeadStatus.__repr__` method in the `LeadStatus` class is likely used to provide a string representation of the `LeadStatus` object. This method is called internally by Python when it needs to represent the object in a string format, such as when printing the object.

---

## 🔹 `LeadSource.get_by_id`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:28`

**Description**:
The `LeadSource.get_by_id` method in the `LeadSource` class is used to retrieve a lead source based on its unique identifier, `lead_source_id`. It is likely called by other methods or functions that need to fetch specific lead source details from the database in the EeazyCRM application.

---

## 🔹 `LeadSource.lead_source_query`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:32`

**Description**:
The `LeadSource.lead_source_query` method in the `LeadSource` class appears to be a method related to querying lead sources in a CRM system, possibly retrieving or manipulating data related to where leads are coming from. The specific caller of this method is not provided in the context.

---

## 🔹 `LeadSource.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:35`

**Description**:
The `LeadSource.__repr__` method in the `LeadSource` class is likely used to provide a string representation of an instance of the class. This method is typically called by built-in Python functions and operators that need to convert the object to a string for display.

---

## 🔹 `Lead.get_by_id`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:60`

**Description**:
The `Lead.get_by_id` method in the `Lead` class is used to retrieve a lead record from the database using its unique identifier, `lead_id`. It is likely called by other methods or functions that need to fetch specific lead details.

---

## 🔹 `Lead.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\leads\models.py:63`

**Description**:
The `Lead.__repr__` method in the `Lead` class is used to provide a string representation of the Lead object. It is automatically called by Python when a string representation of the object is needed, such as when printing the object.

---

## 🔹 `reset_lead_filters`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:22`

**Description**:
The `reset_lead_filters` method is used to clear or reset the filters applied to the leads in the EeazyCRM application. It is likely called by a user or system process when there is a need to view all leads without any applied filters.

---

## 🔹 `get_leads_view`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:38`

**Description**:
The `get_leads_view` method is used to retrieve and filter lead data based on various parameters like search, owner, date, source, and status, and also checks access permissions. It is likely called by a controller or a route handler in the EeazyCRM application.

---

## 🔹 `new_lead`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:76`

**Description**:
The `new_lead` method is likely used to create a new lead in the EeazyCRM system. It is probably called by a user or system process, and it also calls the 'check_access' method, presumably to verify permissions.

---

## 🔹 `update_lead`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:107`

**Description**:
The `update_lead` method is likely called by a CRM system to update the status or details of a specific lead, identified by 'lead_id'. It checks access permissions before proceeding with the update using 'LeadStatus.get_by_id' and 'check_access' methods.

---

## 🔹 `get_lead_view`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:161`

**Description**:
The `get_lead_view` method is likely used to retrieve the view or details of a specific lead identified by 'lead_id' in a CRM system. It is probably called by other methods or functions that need to display or process lead information, after checking access permissions.

---

## 🔹 `delete_lead`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:169`

**Description**:
The `delete_lead` method is used to delete a specific lead from the system using the provided 'lead_id'. It is likely called by an administrator or a user with sufficient permissions, as it checks for access before proceeding with the deletion.

---

## 🔹 `convert_lead`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:186`

**Description**:
The `convert_lead` method is likely used in the EeazyCRM application to convert a lead, identified by 'lead_id', into a customer or a different status. It is probably called by other methods or functions within the application that handle lead management and it checks access before performing the conversion.

---

## 🔹 `import_bulk_leads`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:224`

**Description**:
The `import_bulk_leads` method is likely used to import a large number of leads into the system at once. It is unclear who calls this method based on the provided context.

---

## 🔹 `bulk_owner_assign`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:258`

**Description**:
The `bulk_owner_assign` method is likely used to assign multiple items or tasks to a specific owner in the EeazyCRM system. It's probably called by other methods or functions that handle task or item assignments in bulk.

---

## 🔹 `bulk_lead_source_assign`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:280`

**Description**:
The `bulk_lead_source_assign` method is likely used to assign a source to multiple leads at once in the EeazyCRM system. It is unclear who calls this method without additional context.

---

## 🔹 `bulk_lead_status_assign`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:302`

**Description**:
The `bulk_lead_status_assign` method is likely used to assign statuses to a bulk of leads in the EeazyCRM system. It's probably called by other methods or functions that handle lead management in the CRM.

---

## 🔹 `bulk_delete`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:323`

**Description**:
The `bulk_delete` method is likely used to delete multiple items at once in the EeazyCRM application, specifically within the leads section. It's not specified who calls this method, but it's likely called by an administrator or a user with sufficient permissions.

---

## 🔹 `write_to_csv`
**Location**: `..\EeazyCRM\eeazycrm\leads\routes.py:340`

**Description**:
The `write_to_csv` method is likely used to export data into a CSV format. The method is probably called by other functions or methods within the EeazyCRM application, specifically within the leads module.

---

## 🔹 `home`
**Location**: `..\EeazyCRM\eeazycrm\main\routes.py:14`

**Description**:
The 'home' method in the file routes.py of the EeazyCRM application seems to be responsible for rendering the home page of the application. It's likely called when a user navigates to the home page of the application.

---

## 🔹 `create_db`
**Location**: `..\EeazyCRM\eeazycrm\main\routes.py:19`

**Description**:
The `create_db` method is likely used to initialize or create a new database for the EeazyCRM application. It's not specified who calls this method, but it could be called during the setup or initialization process of the application.

---

## 🔹 `is_allowed`
**Location**: `..\EeazyCRM\eeazycrm\rbac\__init__.py:15`

**Description**:
The `is_allowed` method is used to check if a certain role (identified by 'role_id') has the permission to perform a specific 'action' on a certain 'resource'. It's likely called by other methods or functions that need to verify permissions before proceeding with an action in the EeazyCRM system.

---

## 🔹 `check_access`
**Location**: `..\EeazyCRM\eeazycrm\rbac\__init__.py:43`

**Description**:
The `check_access` method is used to verify if a certain action is permitted on a specific resource. It is likely called by various parts of the EeazyCRM system whenever an action needs to be performed on a resource to ensure proper access control.

---

## 🔹 `decorator`
**Location**: `..\EeazyCRM\eeazycrm\rbac\__init__.py:67`

**Description**:
The `decorator` method in the EeazyCRM application is likely used to add additional functionality or modify the behavior of other functions or methods, specifically related to role-based access control (RBAC), as it calls the 'is_allowed' method. It's called by any function or method that requires this additional RBAC functionality.

---

## 🔹 `decorated_function`
**Location**: `..\EeazyCRM\eeazycrm\rbac\__init__.py:46`

**Description**:
The `decorated_function` method is likely used as a decorator to add additional functionality, such as access control, to other functions in the EeazyCRM application. It is called by any function that requires the additional functionality provided by this decorator, specifically the 'is_allowed' check.

---

## 🔹 `is_admin`
**Location**: `..\EeazyCRM\eeazycrm\rbac\__init__.py:65`

**Description**:
The `is_admin` method is likely used to check if a certain function or user has administrative privileges in the EeazyCRM application. It would be called whenever there's a need to verify if a user or function has admin rights.

---

## 🔹 `deal_reports`
**Location**: `..\EeazyCRM\eeazycrm\reports\routes.py:17`

**Description**:
The `deal_reports` method is likely used to handle or manage reports related to deals in the EeazyCRM application. It is probably called by other methods or routes within the application that need to generate, display, or manipulate deal-related reports.

---

## 🔹 `deal_stages`
**Location**: `..\EeazyCRM\eeazycrm\reports\routes.py:23`

**Description**:
The `deal_stages` method seems to be related to the functionality of managing or processing different stages of a deal in the EeazyCRM application. The specific caller of this method is not provided in the context.

---

## 🔹 `deals_closed`
**Location**: `..\EeazyCRM\eeazycrm\reports\routes.py:52`

**Description**:
The `deals_closed` method is likely used to generate or retrieve a report or data related to closed deals in the EeazyCRM system. It's unclear who calls this method without additional context, but it could be called by other methods or routes within the CRM system that need this information.

---

## 🔹 `get_users_deals`
**Location**: `..\EeazyCRM\eeazycrm\reports\routes.py:94`

**Description**:
The `get_users_deals` method is likely used to retrieve the deals associated with a specific user in the EeazyCRM system. The method caller could be any part of the system that needs to access user-specific deal information.

---

## 🔹 `deal_stage_by_users`
**Location**: `..\EeazyCRM\eeazycrm\reports\routes.py:116`

**Description**:
The `deal_stage_by_users` method appears to be used for generating a report related to the stages of deals associated with different users in a CRM system. It's likely called by a reporting or analytics component within the EeazyCRM application.

---

## 🔹 `deal_closed_by_date`
**Location**: `..\EeazyCRM\eeazycrm\reports\routes.py:153`

**Description**:
The `deal_closed_by_date` method is likely used to fetch or calculate information about deals that were closed on a specific date in the EeazyCRM application. The specific caller of this method is not provided in the context.

---

## 🔹 `test`
**Location**: `..\EeazyCRM\eeazycrm\settings\app_routes.py:16`

**Description**:
The `test` method in the file `app_routes.py` does not belong to any class, takes no arguments, and does not return anything. It's unclear who calls this method, but given its name and location, it's likely used to conduct some form of testing within the EeazyCRM application.

---

## 🔹 `date_format_query`
**Location**: `..\EeazyCRM\eeazycrm\settings\forms.py:8`

**Description**:
The method `date_format_query` does not provide enough context to determine its purpose. The method is located in the settings of the EeazyCRM project, suggesting it might be related to formatting date queries within the CRM system. However, without knowing what the method does or who calls it, a definitive purpose cannot be determined.

---

## 🔹 `email_enc_query`
**Location**: `..\EeazyCRM\eeazycrm\settings\forms.py:13`

**Description**:
The `email_enc_query` method appears to be related to handling email encryption queries in the EeazyCRM application. However, without more context or information about what the method does, it's not possible to provide a more specific description. The method caller is not specified in the provided context.

---

## 🔹 `Currency.get_list_query`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:15`

**Description**:
The `Currency.get_list_query` method in the `Currency` class is likely used to retrieve a list of all currency data from the database. It is called by any part of the EeazyCRM application that needs to access or display this list of currencies.

---

## 🔹 `Currency.get_currency_by_id`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:19`

**Description**:
The method `Currency.get_currency_by_id` in the `Currency` class is used to retrieve a specific currency using its unique identifier, `currency_id`. It is called by any part of the program that needs to fetch details of a specific currency in the EeazyCRM application.

---

## 🔹 `Currency.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:22`

**Description**:
The `Currency.__repr__` method in the `Currency` class is likely used to provide a string representation of the Currency object. This method is typically called by Python's built-in functions and operators when they need to generate a string representation of the object.

---

## 🔹 `TimeZone.get_list_query`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:31`

**Description**:
The `TimeZone.get_list_query` method in the `TimeZone` class is likely used to retrieve a list of all time zones. The specific caller of this method is not provided in the context.

---

## 🔹 `TimeZone.get_tz_by_id`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:35`

**Description**:
The `TimeZone.get_tz_by_id` method in the `TimeZone` class is used to retrieve a specific timezone based on its 'tz_id'. It is likely called by other methods or classes within the EeazyCRM application that require timezone information.

---

## 🔹 `TimeZone.get_tz_by_name`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:39`

**Description**:
The `TimeZone.get_tz_by_name` method in the `TimeZone` class is used to retrieve a specific timezone by its name. It is called by any part of the program that requires information about a specific timezone.

---

## 🔹 `TimeZone.__repr__`
**Location**: `..\EeazyCRM\eeazycrm\settings\models.py:42`

**Description**:
The `TimeZone.__repr__` method in the `TimeZone` class is likely used to provide a string representation of the TimeZone object for debugging or logging purposes. It is called by the Python interpreter when a representation of the object is needed.

---

## 🔹 `settings_profile`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:18`

**Description**:
The `settings_profile` method is likely used to manage or update the settings of a user's profile in the EeazyCRM application. It is probably called by the user interface when a user wants to change their profile settings, and it includes functionality for uploading a new avatar.

---

## 🔹 `settings_staff_list`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:42`

**Description**:
The `settings_staff_list` method is likely used to retrieve a list of staff settings in the EeazyCRM application. It is probably called by other methods or functions that require information about staff settings, after checking access permissions.

---

## 🔹 `settings_staff_view`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:55`

**Description**:
The `settings_staff_view` method is likely called by a part of the CRM system to manage the settings view for a specific staff member, identified by their 'user_id'. It may also perform an access check for the user using the 'check_access' method.

---

## 🔹 `settings_staff_update`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:63`

**Description**:
The `settings_staff_update` method is likely called by an administrator or manager within the EeazyCRM application to update the settings of a staff member, identified by their 'user_id'. It may involve uploading a new avatar and checking access permissions.

---

## 🔹 `settings_staff_new`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:137`

**Description**:
The `settings_staff_new` method is likely used to create new staff settings in the EeazyCRM application. It is probably called by an administrator or a user with sufficient privileges, and it involves uploading an avatar and checking access permissions.

---

## 🔹 `settings_staff_remove`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:167`

**Description**:
The `settings_staff_remove` method is used to remove a staff member from the settings in the EeazyCRM application, identified by their 'user_id'. It is likely called by an admin or a user with sufficient privileges, after checking access rights.

---

## 🔹 `settings_staff_remove_by_email`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:176`

**Description**:
The `settings_staff_remove_by_email` method is used to remove a staff member from the settings of the EeazyCRM application using their email address. It is likely called by an administrator or a user with sufficient privileges, as it involves a 'check_access' call to ensure the user has the necessary permissions.

---

## 🔹 `email_settings`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:185`

**Description**:
The `email_settings` method is likely used to configure or manage email settings in the EeazyCRM application. It's not clear who calls this method based on the provided context.

---

## 🔹 `settings_roles_view`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:193`

**Description**:
The `settings_roles_view` method is likely used to display the settings related to different roles in the EeazyCRM application. It is probably called when a user navigates to the roles settings page in the application.

---

## 🔹 `settings_roles_new`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:206`

**Description**:
The `settings_roles_new` method is likely used to create new roles in the settings of the EeazyCRM application. The specific caller of this method is not provided in the context.

---

## 🔹 `settings_roles_update`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:245`

**Description**:
The `settings_roles_update` method is used to update the permissions of a specific role in the EeazyCRM system. It is likely called by a system administrator or other user with sufficient privileges.

---

## 🔹 `settings_roles_remove`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:284`

**Description**:
The `settings_roles_remove` method is used to remove a specific role from the settings in the EeazyCRM application, identified by its 'role_id'. It is likely called by an administrator or a user with sufficient permissions when they want to delete a role from the system.

---

## 🔹 `create_resource`
**Location**: `..\EeazyCRM\eeazycrm\settings\routes.py:295`

**Description**:
The `create_resource` method is likely used to create a new resource in the EeazyCRM application. The specific caller of this method is not provided in the context.

---

## 🔹 `Register.validate_username`
**Location**: `..\EeazyCRM\eeazycrm\users\forms.py:27`

**Description**:
The `Register.validate_username` method in the `Register` class is used to check the validity of a username when a user is trying to register. It is called when a new user is trying to sign up in the EeazyCRM application.

---

## 🔹 `Register.validate_email`
**Location**: `..\EeazyCRM\eeazycrm\users\forms.py:32`

**Description**:
The `Register.validate_email` method in the `Register` class is used to validate the email provided by the user during the registration process. It is likely called when a new user is trying to register in the EeazyCRM system.

---

## 🔹 `NewRoleForm.validate_name`
**Location**: `..\EeazyCRM\eeazycrm\users\forms.py:74`

**Description**:
The `NewRoleForm.validate_name` method in the `NewRoleForm` class is used to validate the 'name' argument, likely ensuring it meets certain criteria or doesn't already exist in the system. It is called by any instance of the `NewRoleForm` class.

---

## 🔹 `load_user`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:6`

**Description**:
The `load_user` method is likely used to retrieve a user's information based on their `user_id` from the database in the EeazyCRM application. It is probably called whenever user-specific data is needed, such as during user authentication or profile viewing.

---

## 🔹 `User.get_label`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:27`

**Description**:
The `User.get_label` method in the `User` class is likely used to retrieve a label for a specific user, possibly by calling the `User.get_name` method to get the user's name. This method is called on an instance of the `User` class.

---

## 🔹 `User.user_list_query`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:31`

**Description**:
The `User.user_list_query` method in the `User` class is likely used to generate or handle a query related to a list of users in the EeazyCRM application. It's probably called by other methods or functions that need to retrieve or manipulate user data.

---

## 🔹 `User.get_current_user`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:35`

**Description**:
The `User.get_current_user` method in the `User` class is likely used to retrieve the currently logged in or active user in the EeazyCRM application. It is probably called by various parts of the application where user-specific information or actions are required.

---

## 🔹 `User.get_by_id`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:39`

**Description**:
The `User.get_by_id` method in the `User` class is used to retrieve a user's details based on their unique user ID. It is likely called whenever user-specific information is needed, such as during user profile viewing or editing.

---

## 🔹 `User.get_name`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:42`

**Description**:
The `User.get_name` method in the `User` class is likely used to retrieve the name of a user. It is called by any instance of the `User` class that needs to access the user's name.

---

## 🔹 `Role.get_by_name`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:72`

**Description**:
The `Role.get_by_name` method in the `Role` class is used to retrieve a role based on its name. It is called by any function or method that needs to fetch a role's details using its name in the EeazyCRM application.

---

## 🔹 `Role.get_by_id`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:76`

**Description**:
The `Role.get_by_id` method in the `Role` class is used to retrieve a specific role based on its `role_id`. It is called by any function or method that requires to fetch role details using the role's unique identifier.

---

## 🔹 `Role.set_permissions`
**Location**: `..\EeazyCRM\eeazycrm\users\models.py:79`

**Description**:
The `Role.set_permissions` method in the `Role` class is used to assign specific permissions to a role in the EeazyCRM application. It is likely called by an administrator or a function that manages user roles and permissions.

---

## 🔹 `login`
**Location**: `..\EeazyCRM\eeazycrm\users\routes.py:13`

**Description**:
The `login` method is likely used to handle the login process for users in the EeazyCRM application. It's probably called when a user attempts to log in to the system.

---

## 🔹 `register`
**Location**: `..\EeazyCRM\eeazycrm\users\routes.py:37`

**Description**:
The `register` method is likely used to handle the registration process of new users in the EeazyCRM application. It is probably called when a new user attempts to create an account.

---

## 🔹 `logout`
**Location**: `..\EeazyCRM\eeazycrm\users\routes.py:57`

**Description**:
The `logout` method is used to log out a user from the EeazyCRM application. It is likely called when a user chooses to log out of their session.

---

## 🔹 `upload_avatar`
**Location**: `..\EeazyCRM\eeazycrm\users\utils.py:8`

**Description**:
The `upload_avatar` method is used to upload a user's avatar or profile picture. It is likely called when a user updates their profile picture in the EeazyCRM application.

---
