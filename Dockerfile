FROM node:10 AS frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

FROM nginx:alpine as nginx
COPY --from=frontend /app/dist /usr/share/nginx/html
COPY config/nginx.conf /etc/nginx/nginx.conf