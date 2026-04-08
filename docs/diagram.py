from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.custom import Custom

with (Diagram(show=False, filename="diagram")):
    user = Users("Usuario\n(Navegador Web)")
    with Cluster("Docker / Red docker-compose"):
        with Cluster("WebApp") as webapp:
            vanillaJS = Custom("Vanilla JS","./icons/javascript.png")
            springBoot = Custom("Spring Boot","./icons/spring.png")
        with Cluster("DB"):
            postgres = Custom("PostgreSQL", "./icons/postgresql.png")
        with Cluster("Ollama"):
            with Cluster(""):
                qwen = Custom("LLM","./icons/gemma.png")
    nominatim = Custom("Nominatim","./icons/openstreetmap.png")
    # mediawiki = Custom("MediaWiki","./icons/mediawiki.png")
    springBoot >> postgres
    springBoot >> qwen
    user >> Edge(label="HTTP") >> vanillaJS
    vanillaJS >> springBoot
    springBoot >> nominatim
