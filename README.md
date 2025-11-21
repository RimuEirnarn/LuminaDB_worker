# LuminaDB Worker

Worker thread extension for **LuminaDB**.

## Install

Use `pip install luminadb_worker`

## Usage?

```python

from uuid import uuid4
from luminadb import model, BaseModel, Primary
from luminadb_worker import DatabaseWorker

db = DatabaseWorker(":memory:")

@model(db)
class Users(BaseModel):
    __schema__ = (Primary('id'),)
    __auto_id__ = lambda: str(uuid4())
    
    id: str
    username: str
    password: str
```
