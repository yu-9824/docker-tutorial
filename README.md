# docker-tutorial
This is my Docker's tutorial.
## Install (mac)
- [Download](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- [Reference](https://docs.docker.com/docker-for-mac/install/)

## Hello world
### Script
```bash
docker container run ubuntu:latest /bin/echo 'Hello world'
```
### Results
#### 1st time
```
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
6f86eded34a1: Pull complete 
Digest: sha256:aba80b77e27148d99c034a987e7da3a287ed455390352663418c0f2ed40417fe
Status: Downloaded newer image for ubuntu:latest
Hello world
```

#### After 2nd time
```
Hello world
```

## Check version
### Script
```bash
docker version
```

## Dockerの実行環境 (Excecution environment)
### Script
```bash
docker system info
```
### Results (Excerpt.)
```
Server:
 Containers: 2  # Number of containers
 ...
 Server Version: 20.10.7    # Dockerのバージョン
 Storage Driver: overlay2   # ストレージドライバーの種類
 ...
 OSType: linux  # OSの種類
 Architecture: aarch64  # アーキテクチャ
```

## Dockerのディスクの利用状況
```bash
docker system df
```

### Results
```
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          1         1         65.55MB   0B (0%)
Containers      2         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B
```

## Tutorials (Ngixを使った例)
### Download the Docker image
```bash
docker pull nginx
```

### イメージを使ってNginxのサーバーを起動
```bash
docker container run --name webserver -d -p 80:80 nginx
```

### サーバー状態の確認
```bash
docker container ps
```

### コンテナ起動の確認
```bash
docker container stats webserver
```

### コンテナの停止
```bash
docker stop webserver
```

### コンテナの起動
```bash
docker start webserver
```
