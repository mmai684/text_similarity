FROM python:3
RUN pip install flask
RUN pip install requests
ADD textsim.py /
ADD flask_text_sim.py /
ADD flask_sim_api_call.py /
CMD ["python","./flask_text_sim.py"]