# Import process

Import process loads digital objects into repository.

## Input

- XML files (Fedora format)
- each file represents a page

## Behavior

- parses input XML
- stores objects into Akubra repository
- updates repository structure

## Output

- repository objects
- triggers Index process

## Notes

- Import does not update search index directly
- indexing is delegated to Index process