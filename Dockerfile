FROM python:3.8-slim-buster

# Create workdir
RUN mkdir /app
WORKDIR /app

# Run some magic
COPY Pip* /app/
RUN pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

# Expose to default flask port
EXPOSE 5000
CMD flask run --host=0.0.0.0