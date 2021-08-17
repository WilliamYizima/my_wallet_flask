FROM python:3.8
WORKDIR /app
COPY . .
RUN make install
RUN make create-db
ENV SECRET_KEY=xxx
EXPOSE 5000
CMD ["make","run"]
