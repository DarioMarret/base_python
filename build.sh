
git add .

git commit -m "ajustes de configuracion"

git push

export SHORT_COMMIT=$(git log -1 --pretty="%H" | cut -b -8)
export DOCKER_IMAGE_VERSION="dev_${SHORT_COMMIT}"

# docker build -t intelnexoec/ejemplo:${DOCKER_IMAGE_VERSION} -f Dockerfile .
# docker tag intelnexoec/ejemplo:${DOCKER_IMAGE_VERSION} intelnexoec/ejemplo:latest
# docker push intelnexoec/ejemplo:${DOCKER_IMAGE_VERSION}
# docker push intelnexoec/ejemplo:latest
# echo "tag: ${DOCKER_IMAGE_VERSION}"

# docker build -t xtrim-api-informacion -f Dockerfile .
# docker run -p 3003:3003 xtrim-api-informacion