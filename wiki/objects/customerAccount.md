# customerAccount

A registration of the TRANSPORT CUSTOMER with an ACCOUNT PROVIDER to obtain travel services.

**Type:** `object`

semantics [{'transmodel': 'CUSTOMER ACCOUNT'}]

---

## Properties overview

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | [customerReference](customerReference.md) |  | default string, full names etc (length 0-200) |
| `customer` | [customer](customer.md) |  | A user that wishes to purchase a package |
| `creationDate` | [dateTime](dateTime.md) |  | The date in which the CUSTOMER ACCOUNT has been created |
| `modificationDate` | [dateTime](dateTime.md) |  | Last modification date of CUSTOMER ACCOUNT. |
| `status` | [customerAccountStatus](customerAccountStatus.md) |  | The status of the CUSTOMER ACCOUNT |

## Detailed Properties

- **`id`**  *([customerReference](customerReference.md))* - optional  
  default string, full names etc (length 0-200)

- **`customer`**  *([customer](customer.md))* - optional  
  A user that wishes to purchase a package
  - **`id`**  *(string)* - **required**  
    The identifier the MP uses to identify the customer. Could be an external referenced ID, like a ABT account number
  - **`initials`**  *(string)* - optional  
    Initials of the customer
  - **`firstName`**  *(string)* - optional  
    First name of the customer
  - **`lastName`**  *(string)* - optional  
    Last name of the customer
  - **`middleName`**  *(string)* - optional  
    Middle name of the customer
  - **`prefix`**  *(string)* - optional  
    prefix of the customer, like titles
  - **`postfix`**  *(string)* - optional  
    postfix of the customer, like titles
  - **`phoneNumber`**  *(string)* - optional  
    default string, full names etc (length 0-200)
  - **`email`**  *(string)* - optional  
    the email address of the customer
  - **`dateOfBirth`**  *(string (full-date))* - optional  
    https://www.rfc-editor.org/rfc/rfc3339#section-5.6, full-date (2019-10-12)
  - **`placeOfBirth`**  *(string)* - optional  
    short string, display names (length 0-75)
  - **`countryOfBirth`**  *(string)* - optional  
    short string, display names (length 0-75)
  - **`address`**  *(object)* - optional  
    address parts, where addressLine1 and 2 should contain the complete address, matches Content-Language
  - **`photo`**  *(string)* - optional  
  - **`customFields`**  *(object)* - optional  
    dictionary for extra fields (bilatural agreements)

- **`creationDate`**  *([dateTime](dateTime.md))* - optional  
  The date in which the CUSTOMER ACCOUNT has been created

- **`modificationDate`**  *([dateTime](dateTime.md))* - optional  
  Last modification date of CUSTOMER ACCOUNT.

- **`status`**  *([customerAccountStatus](customerAccountStatus.md))* - optional  
  The status of the CUSTOMER ACCOUNT

## Example

```json
{
  "id": "identifier",
  "customer": {
    "id": "identifier",
    "initials": "example-string",
    "firstName": "example-string",
    "lastName": "example-string"
  },
  "creationDate": "2024-01-15T10:30:00Z"
}
```

