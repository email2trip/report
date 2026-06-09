from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.custom import Custom

graph_attr = {
    "nodesep": "0.35",
    "ranksep": "0.45",
    "pad": "0.25",
    "margin": "0.25",
}

cluster_attr = {
    "margin": "1",
}

node_attr = {
    "margin": "0.02,0.02",
}

with Diagram(show=False, filename="diagram", graph_attr=graph_attr, node_attr=node_attr):
    user = Users("Usuario\n(Navegador Web)")
    with Cluster("Docker / Red docker-compose", graph_attr=cluster_attr):
        with Cluster("WebApp", graph_attr=cluster_attr):
            vanillaJS = Custom("Vanilla JS", "./icons/javascript.png")
            springBoot = Custom("Spring Boot", "./icons/spring.png")
        with Cluster("DB", graph_attr=cluster_attr):
            postgres = Custom("PostgreSQL", "./icons/postgresql.png")
        with Cluster("Ollama", graph_attr=cluster_attr):
            llm = Custom(
                "LLM",
                "./icons/gemma.png",
                shape="box",
                style="rounded,filled",
                fillcolor="#f3ecff",
                color="#c8b8e8",
                penwidth="2",
                margin="0.08,0.04",
            )
    nominatim = Custom("Nominatim", "./icons/openstreetmap.png")
    springBoot >> postgres
    springBoot >> llm
    user >> Edge(label="HTTP") >> vanillaJS
    vanillaJS >> springBoot
    springBoot >> nominatim
