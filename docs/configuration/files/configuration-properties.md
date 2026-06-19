[Index](../index) / [Konfigurace](../../configuration)  / [Soubory](../../configuration/files)

# Configuration Properties

TODO

The primary `configuration.properties` file contains the core runtime configuration of the Kramerius platform.

This page documents the most important and commonly customized properties.

For the list of configuration files, see [Configuration Files](index).

---

# Database configuration

Database connectivity used by the application and internal services.

## Example

jdbcUrl=jdbc:postgresql://localhost/kramerius4  
jdbcUserName=fedoraAdmin  
jdbcUserPass=fedoraAdmin

## Important properties

| Property | Description |
|---|---|
| jdbcUrl | JDBC connection URL |
| jdbcUserName | Database username |
| jdbcUserPass | Database password |
| jdbcMaximumPoolSize | Maximum JDBC pool size |
| jdbcConnectionTimeout | Connection timeout in milliseconds |

---

# Search configuration

Configuration of Solr search indexes.

## Example

solrSearchHost=http://localhost:8983/solr/search  
solrProcessingHost=http://localhost:8983/solr/processing

## Important properties

| Property | Description |
|---|---|
| solrSearchHost | Public search index |
| solrProcessingHost | Processing index |
| solrSearchLogin | Solr username |
| solrSearchPassword | Solr password |

## Notes

The older solrHost property is deprecated.

---

# Fedora configuration

Fedora repository connectivity.

## Example

fedoraHost=${_fedoraTomcatHost}/fedora  
fedoraUser=fedoraAdmin  
fedoraPass=fedoraAdmin

## Important properties

| Property | Description |
|---|---|
| fedoraHost | Fedora repository URL |
| fedoraUser | Fedora username |
| fedoraPass | Fedora password |

---

# API configuration

Public and administration API endpoints.

## Example

api.client.point=${applicationUrl}/api/client/v7.0  
api.admin.v7.point=${applicationUrl}/api/admin/v7.0

---

# Processing configuration

Background processing and process queue settings.

## Example

processQueue.checkInterval=10000  
processManagerUrl=${processManagerHost}/process-manager/api

## Important properties

| Property | Description |
|---|---|
| processQueue.checkInterval | Process scheduler polling interval |
| processManagerUrl | Process Manager API URL |
| generatePdfMaxRange | Maximum generated PDF range |

---

# Storage configuration

Filesystem and object storage configuration.

## Example

objectStore.path=${sys:user.home}/.kramerius4/data/objectStore  
datastreamStore.path=${sys:user.home}/.kramerius4/data/datastreamStore

## Important properties

| Property | Description |
|---|---|
| objectStore.path | Object storage location |
| datastreamStore.path | Datastream storage location |
| deepZoom.cachedir | Deep Zoom tile cache |

---

# Security configuration

Authentication and secured datastream configuration.

## Example

keycloak.realm=kramerius  
securedstreams=TEXT_OCR

## Important properties

| Property | Description |
|---|---|
| keycloak.realm | Keycloak realm |
| keycloak.clientId | OAuth client ID |
| securedstreams | Protected datastreams |

---

# Deprecated properties

Some properties remain for backward compatibility and should not be used in new deployments.

| Property | Status |
|---|---|
| solrHost | Deprecated |
| fullImage.scalingMethod | Deprecated |
| fullImage.iterateScaling | Deprecated |