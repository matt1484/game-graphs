FROM node:16 AS base

WORKDIR /ui
COPY . .

RUN npm install
RUN node_modules/.bin/ng build

ENTRYPOINT ["/ui/node_modules/.bin/ng", "serve", "--port", "80", "--host", "0.0.0.0"]



# if I were to deploy this this would make more sense than running `ng serve` like above
FROM nginx:latest

COPY --from=base /ui/dist/game-graphs /usr/share/nginx/html
EXPOSE 80