ONE
docker tag <image_name> docker.pkg.github.com/<GitHub username>/<repository name>/<image_name>:<version>

docker push docker.pkg.github.com/<GitHub username>/<repository name>/<image_name>:<version>

docker tag alpnsecuresql gcr.io/rdrtest/alpnsecuresql:1.0
docker push alpnsecuresql gcr.io/rdrtest/myimage