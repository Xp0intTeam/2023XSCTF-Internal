FROM node:18-alpine

RUN apk add --no-cache chromium

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

COPY ./app /app
WORKDIR /app
RUN npm install --registry https://registry.npmmirror.com/
RUN npm install puppeteer --save-dev --registry https://registry.npmmirror.com/

CMD ["node", "main.js"]