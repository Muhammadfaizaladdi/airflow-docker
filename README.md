# airflow-docker

## Running Airflow in Docker

Dokumen ini berisi panduan dasar untuk menginstal Airflow pada komputer Anda menggunakan Docker, airflow akan dijalankan pada CeleryExecutor. Dokumen ini diperuntukkan untuk pengguna Airflow tahap awal untuk menjadi lebih familiar terhadap database system Airflow.

## Sebelum Dimulai

Ikuti langkah-langkah ini untuk menginstal dependencies yang diperlukan.

- Instal [Docker Community Edition (CE)](https://docs.docker.com/engine/install/) di workstation Anda. Bergantung pada OS, kamu mungkin perlu mengonfigurasi instance Docker untuk menggunakan memori 4,00 GB agar semua container berjalan dengan benar. Silakan merujuk ke Resources section jika menggunakan [Docker for Windows](https://docs.docker.com/desktop/windows/) atau [Docker for Mac](https://docs.docker.com/desktop/mac/) untuk informasi selengkapnya.
- Instal [Docker Compose v1.29.1](https://docs.docker.com/compose/install/) atau yang lebih update di workstation kamu.

## docker-compose.yaml

Untuk men-deploy Airflow di Docker Compose, Anda harus mengunduh [docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml). Atau menggunakan command curl berikut. 
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.2/docker-compose.yaml'
```
