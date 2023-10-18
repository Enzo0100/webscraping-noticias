#!/bin/bash

# Construir a imagem Docker
docker build -t api-noticias-server .

# Se a construção foi bem-sucedida, execute o container
if [ $? -eq 0 ]; then
    docker run -p 6060:6060 api-noticias-server
else
    echo "Erro na construção da imagem Docker. Container não iniciado."
fi
#!/bin/bash