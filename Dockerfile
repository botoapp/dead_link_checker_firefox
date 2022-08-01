FROM public.ecr.aws/george-lim/firefox-lambda:1.1.0

ENV XVFB_WHD=1280x720x16

COPY app.py $LAMBDA_TASK_ROOT

RUN pip install requests

CMD ["app.handler"]