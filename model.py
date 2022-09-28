from pydantic import BaseModel

from typing import Union

class Developer(BaseModel):
    name: str
    tnumber: str
    main_skill: Union[str, None]
    salary: Union[float, None]
    