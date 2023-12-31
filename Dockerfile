# Using lightweight alpine image
FROM python:3.12-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock run.sh ./
COPY products-worker ./products-worker

# Install API dependencies
RUN pipenv install --system --deploy

# Start app
EXPOSE 8000
ENTRYPOINT ["/usr/src/app/run.sh"]