# Dockerfile
FROM node:16

# 作業ディレクトリを設定
WORKDIR /app

# アプリの依存関係をインストール
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

# アプリソースをコピー
COPY . ./

# ビルド
RUN npm run build

# サーブ用に nginx を利用
FROM nginx:stable-alpine
COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]