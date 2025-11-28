npx @openapitools/openapi-generator-cli generate -i .\TOMP-API.yaml `
    -g spring `
    -o c:/sources/TOMP/v2 `
    --additional-properties=apiPackage=org.tomp.api `
    --additional-properties=modelPackage=org.tomp.model `
    --additional-properties=configPackage=org.tomp.config `
    --additional-properties=packageName=org.tomp.api `
    --additional-properties=group-id=org.tomp `
    --additional-properties=artifact-id=tomp-api `
    --additional-properties=version=2.0.0 `
    --additional-properties=basePackage=org.tomp `
    --additional-properties=dateLibrary=java8 `
    --additional-properties=documentationProvider=springdoc

#npx @openapitools/openapi-generator-cli generate -i .\TOMP-API.yaml `
    #-g plantuml `
    #-o c:/sources/TOMP/v2/plantuml
