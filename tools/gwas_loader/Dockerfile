FROM python:3.10-slim

# Install required libraries
RUN pip install gwaslab pandas polars

WORKDIR /opt/gwas_loader

COPY gwas_loader.py .

ENTRYPOINT ["python", "/opt/gwas_loader/gwas_loader.py"]
