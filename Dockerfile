FROM python

ENV username_github=chips-wq token_github=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 base_dir_github=https://api.github.com/repos/chips-wq/Exercitii-Informatica-Clasa-10A/contents token_bot=ODI2Nzg4MTk5ODcwMzY1Nzc2.YGRkgw.w_5uklhGjK5GNXMJorWduvSv0S0

RUN /usr/local/bin/python -m pip install --upgrade pip 
    
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN python3 init_DB.py

CMD [ "python3" , "run.py" ]