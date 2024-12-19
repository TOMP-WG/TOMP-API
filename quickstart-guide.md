redocly join .\TOMP-API.yaml .\TOMP-API-DISCOVERY.yaml -o TOMP-total.yaml --without-x-tag-groups

redocly join TOMP-API.yaml .\TOMP-API-CONTRACT.yaml .\TOMP-API-CUSTOMER.yaml .\TOMP-API-DATASPACES.yaml .\TOMP-API-DISCOVERY.yaml .\TOMP-API-NOTIFY.yaml .\TOMP-API-PAYMENTS.yaml .\TOMP-API-SUPPORT.yaml .\TOMP-API-TECH.yaml -o TOMP-API-total.yaml --without-x-tag-groups