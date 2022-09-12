from dependency_injector import containers, providers
from pysentimiento import create_analyzer

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.api.deps"], packages=["app.api.endpoints"], auto_wire=True
    )

    analizer = providers.Resource(
        create_analyzer,
        task="emotion",
        lang="es"
    )