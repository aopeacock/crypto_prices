FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py main.py
COPY /data/Aave.csv /data/Aave.csv
COPY /data/Bitcoin.csv /data/Bitcoin.csv
COPY /data/Ethereum.csv /data/Ethereum.csv
COPY /data/Solana.csv /data/Solana.csv
COPY /data/Zcash.csv /data/Zcash.csv
CMD ["python", "-u", "main.py"]