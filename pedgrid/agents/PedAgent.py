from pedgrid.agents.Agent import Agent
from typing import Tuple

class PedAgent(Agent):

    def __init__(
        self, 
        id,
        position: Tuple[int, int], 
        direction: int, # TODO convert direction to enum,
        maxSpeed: float = 4,
        speed: float = 3,
        objectType="PedAgent"
        ):
        
        super().__init__(
            id=id,
            topLeft=position,
            bottomRight=position,
            direction=direction,
            maxSpeed=maxSpeed,
            speed=speed,
            objectType=objectType
        )
