FROM alpine:3.20
WORKDIR /src
COPY . .
LABEL org.opencontainers.image.source="https://github.com/mafzalkalwardev/mouse-coordinate-tracker"
CMD ["sh", "-c", "echo 'mouse-coordinate-tracker source package' && ls -1"]
