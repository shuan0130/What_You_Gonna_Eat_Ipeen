
A distributed python crawler using Celery

http://docs.celeryproject.org/en/latest/index.html




## Quick Start

Run the container of Rabbitmq

<br><6_celery_urls_parser>
<br>docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3
<br>celery -A crawler worker --loglevel=info

<br>
<br># Result:
<br>Muti: 236.22525095939636
<br>Single: 1762.2194831371307
