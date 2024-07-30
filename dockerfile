FROM python
WORKDIR./Mangaconverter.py 
COPY. /mangaconverter.py
CMD["python3","Mangaconverter.py"]

