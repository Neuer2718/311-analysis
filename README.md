# 311-analysis
Quick starter for analyzing U.S. 311 service requests.

## Quickstart
```bash
pip install -r requirements.txt
python -m analysis.clean --in data/raw/311_sample.csv --out data/processed/cleaned.csv
python -m analysis.eda --in data/processed/cleaned.csv --plot out/complaints_by_month.png


---

# 3) Create a tiny **synthetic** CSV so the pipeline runs immediately
```bash
cat > data/raw/311_sample.csv << 'EOF'
Created Date,Borough,Incident Zip,Complaint Type,Descriptor
2021-01-15,BROOKLYN,11201,Noise,Car alarm
2021-02-01,MANHATTAN,10027,Street Condition,Pothole
2021-02-14,QUEENS,11373,Heating,No heat
2021-03-07,BRONX,10458,Water System,Water leak
2021-03-21,STATEN ISLAND,10314,Sanitation Condition,Missed Collection
