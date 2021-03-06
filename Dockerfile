FROM python:3.7
MAINTAINER buglan "1831353087@qq.com"
COPY . /code
WORKDIR /code
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv \
    && pipenv install --pypi-mirror https://pypi.tuna.tsinghua.edu.cn/simple \
    && pipenv install --dev --pypi-mirror https://pypi.tuna.tsinghua.edu.cn/simple
CMD pipenv run gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
