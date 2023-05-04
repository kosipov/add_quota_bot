FROM python:3.10-slim
# set work directory
WORKDIR /usr/src/app/

COPY requirements.txt .
# Install the dependencies from the requirements.txt file
RUN pip install -r requirements.txt
# Copy the main.py file to the working directory
COPY add_quota.py .
# copy project
# install dependencies
RUN pip install -r requirements.txt
ENV BOT_TOKEN=YOUR_TOKEN
# run app
CMD ["python", "add_quota.py"]