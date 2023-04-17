FROM python:3.10.0-slim
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
Run pip install argon2_cffi
Run pip install python-jose[cryptography]
Run pip install python-multipart
COPY ./project /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]