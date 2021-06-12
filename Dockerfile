FROM python:3.9.5-slim

WORKDIR /usr/src/app

RUN useradd -u 1234 discord_bot_user

COPY requirements/prod.txt .

RUN pip install --no-cache-dir --requirement prod.txt

USER discord_bot_user

COPY --chown=discord_bot_user:discord_bot_user . .

CMD ["scripts/entrypoint.sh"]
