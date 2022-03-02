FROM python:3.9

RUN pip install fastapi uvicorn
RUN pip install requests

EXPOSE 80

COPY . /app

WORKDIR /app
RUN ls

CMD ["uvicorn", "endpoint:app","--host", "0.0.0.0", "--port", "80", "--reload"]