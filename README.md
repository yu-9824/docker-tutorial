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

## Docker Hubとは
> [Docker Hub](https://hub.docker.com)は、GitHubやBitbucketなどのソースコード管理ツールと連挑してコードをビルドする機能や実行可能なアプリケーションのイメージを管理する機能などを備えたDocker公式のレボジトリサーピスです。


## Dockerfile
DockerコンテナをどのDockerイメージから生成するかについて書いたファイル．

Visual Studio Codeでは，拡張機能[Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)を入れると作成が簡単に．
プログラマのためのDocker教科書 第2版


======================

以下Fork元の内容
> 本リポジトリは、「プログラマのためのDocker教科書 第2版」のサンプル> アプリケーションです。
> 
> ***
> ### 目次
> 
> 1. 押さえておきたいシステムとインフラの基礎知識
> 2. コンテナ技術とDockerの概要
> 3. Dockerのインストールとチュートリアル
> 4. Dockerコマンド
> 5. Dockerfileを使ったコードによるサーバ構築
> 6. Dockerイメージの公開
> 7. 複数コンテナの運用管理
> 8. マルチホスト環境でのDocker実行環境構築
> 9. クラウドを使ったDocker実行環境構築
> 10. クラウドを使ったDocker実行環境の運用管理
> 11. 付録
> 
> ***
> ## 翔泳社公式サイト
> > https://www.seshop.com/product/detail/21503/
> 