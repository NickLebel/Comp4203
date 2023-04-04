# imports
import pandas as pd
from lxml import objectify
import os
import os.path

# settings
pd.options.plotting.backend = "plotly"

# Helper function that coverts an xml file into a pandas dataframe to aid in data processing
def xml_to_pandas_df(filepath):
  xml_data = objectify.parse(filepath)
  root = xml_data.getroot()
  flow_stats = root.getchildren()[0]
  
  data = []
  cols = flow_stats.getchildren()[0].keys()
  for flow in flow_stats.getchildren():
    attributes = []
    for attribute in flow.attrib.values():
      # Convert nanoseconds string to float
      if attribute[-2:] == "ns":
        attributes.append(float(attribute[1:-2]))
      else:
        try:
          attribute = int(attribute)
          attributes.append(attribute)
        except ValueError:
          attributes.append(attribute)
    data.append(attributes)

  df = pd.DataFrame(data) # Write in DF and transpose it
  df.columns = cols  # Update column names
  return df


# Returns average throughput in Kbps
def get_average_throughput(filepath):
  df = pd.read_csv(filepath)
  return df[df['ReceiveRate'] > 0]["ReceiveRate"].mean()


# Returns packet delivery ratio out of 100
def get_packet_delivery_ratio(filepath):
  df = xml_to_pandas_df(filepath)
  df["PDR"] = df.rxPackets.div(df.txPackets)
  return df["PDR"].mean() * 100


# Returns packet loss percentage out of 100
def get_packet_loss_percentage(filepath):
  df = xml_to_pandas_df(filepath)
  df["PLP"] = df.txPackets.sub(df.rxPackets).div(df.txPackets)
  return df["PLP"].mean() * 100

def get_transmission_delay(filepath):
  df = xml_to_pandas_df(filepath)
  delay_in_nano = df["delaySum"].mean()
  return (delay_in_nano / 1000000)


AODV_files = ["Scenario 1/Experiment 1/S1-E1-AODV-20nodes.csv", "Scenario 1/Experiment 1/S1-E1-AODV-30nodes.csv", "Scenario 1/Experiment 1/S1-E1-AODV-50nodes.csv","Scenario 1/Experiment 1/S1-E1-AODV-70nodes.csv"]
other = ["Scenario 1/Experiment 1/S1-E1-DSDV-20nodes.csv",
"Scenario 1/Experiment 1/S1-E1-DSDV-30nodes.csv","Scenario 1/Experiment 1/S1-E1-DSDV-50nodes.csv","Scenario 1/Experiment 1/S1-E1-DSDV-70nodes.csv","Scenario 1/Experiment 1/S1-E1-OLSR-20nodes.csv","Scenario 1/Experiment 1/S1-E1-OLSR-30nodes.csv",
"Scenario 1/Experiment 1/S1-E1-OLSR-50nodes.csv","Scenario 1/Experiment 1/S1-E1-OLSR-70nodes.csv"]

names = ["AODV","DSDV","OLSR"]

def graphPDR(experiment, title, xLabel, yLabel):
  data = {
    "AODV": [],
    "DSDV": [],
    "OLSR": []
  }

  for protocol in data:
    for dirpath, dirnames, filenames in os.walk(f"{experiment}/{protocol}/xml"):
      for filename in filenames:
        file = os.path.join(dirpath, filename)
        pdr = get_packet_delivery_ratio(file)
        data[protocol].append(pdr)

  df = pd.DataFrame.from_dict(data)
  fig = df.plot.line(title=title)
  fig.write_html(f"./graphs/{experiment}-PDR.html")

graphPDR("nodes", "PDR vs Number of nodes", "Number of nodes", "PDR (%)")
