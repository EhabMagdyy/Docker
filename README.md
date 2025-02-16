## Counter Application
##### Python Web Server using Falsk that stores number of page views in redis & display it
---
### Build & Start the docker-compose
```bash
docker-compose up
```
### Stop & Remove the docker-compose
```bash
# Removes (Container & Networks)
docker-compose down
# Removes (Container & Networks & Volums)
docker-compose down -v
# Removes all (Container & Networks & Volums & images)
docker-compose down -v --rmi all
```
---
### Running
> ![Image](https://github.com/user-attachments/assets/8adc7fd4-ec23-4e53-b273-53d05b92364f)
>---
> ![Image](https://github.com/user-attachments/assets/87f7c77b-c18e-473c-8fed-e08cb07bdf07)
>---
---
### redis container connected to internal network, unlike web container that connected to internal & external networks
> ![Image](https://github.com/user-attachments/assets/e2b6a8ad-2460-42e3-a848-c2c401d5d558)
