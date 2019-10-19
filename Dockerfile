FROM python:3.7.2
COPY . /app
WORKDIR /app
RUN pip -V
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement.txt
CMD python DOS/countDos.py
CMD python groupVel/GvFromFinitDiff-x.py
CMD python thermalConductivity/klemens_model-qeinput.py
