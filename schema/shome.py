from pydantic import BaseModel, Field, Json
from typing import List, Optional
from pydantic.schema import schema

class SiteInfo(BaseModel):
    name: Optional[str]
    value: Json

    class Config:
	    orm_mode=True