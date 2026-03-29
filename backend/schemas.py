from pydantic import BaseModel
from typing import List


class GameDesign(BaseModel):
    genre: str
    core_loop: str
    player_goal: str
    mechanics: List[str]



class GameRequest(BaseModel):
    prompt: str