from typing import Any

class AdGroupSimulationServiceStub:
    GetAdGroupSimulation: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupSimulationServiceServicer:
    def GetAdGroupSimulation(self, request: Any, context: Any) -> None: ...

def add_AdGroupSimulationServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
