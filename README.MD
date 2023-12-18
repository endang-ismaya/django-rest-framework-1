# Django REST API Refresher

## When to use APIViews?

- Need full control over the logic
- Processing files and rendering a synchronous response
- You're calling other APIs/services
- Accessing local files or data

## ViewSet?

Methods:

- list(self, request)
- create(self, request)
- retrieve(self, request, pk=None)
- update(self, request, pk=None)
- partial_update(self, request, pk=None)
- destroy(self, request, pk=None)

Function:

- Takes care a lot of typical logic for you
- Perfect for standard database operations
- Fastest way to make a database inteface

When to Use:

- A simple CRUD interface to your database
- A quick and simple API
- Little to no customization on the logic
- Working with standard data structures
