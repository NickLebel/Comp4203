# imports
import pandas as pd
from lxml import objectify
import os
import os.path

# settings
# pd.options.plotting.backend = "plotly"

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


def graphPDR(experiment, title, xLabel, yLabel, xValues):
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
  df.index = xValues
  fig = df.plot(kind="line", title=title, ylabel=yLabel, xlabel=xLabel).get_figure()
  print(df)
  fig.savefig(f"./graphs/{experiment}-PDR")

def graphTransmissionDelay(experiment, title, xLabel, yLabel, xValues):
  data = {
    "AODV": [],
    "DSDV": [],
    "OLSR": []
  }

  for protocol in data:
    for dirpath, dirnames, filenames in os.walk(f"{experiment}/{protocol}/xml"):
      for filename in filenames:
        file = os.path.join(dirpath, filename)
        pdr = get_transmission_delay(file)
        data[protocol].append(pdr)

  df = pd.DataFrame.from_dict(data)
  df.index = xValues
  fig = df.plot(kind="line", title=title, ylabel=yLabel, xlabel=xLabel).get_figure()
  print(df)
  fig.savefig(f"./graphs/{experiment}-transmission-delay")


def graphPacketLoss(experiment, title, xLabel, yLabel, xValues):
  data = {
    "AODV": [],
    "DSDV": [],
    "OLSR": []
  }

  for protocol in data:
    for dirpath, dirnames, filenames in os.walk(f"{experiment}/{protocol}/xml"):
      for filename in filenames:
        file = os.path.join(dirpath, filename)
        pdr = get_packet_loss_percentage(file)
        data[protocol].append(pdr)

  df = pd.DataFrame.from_dict(data)
  df.index = xValues
  fig = df.plot(kind="line", title=title, ylabel=yLabel, xlabel=xLabel).get_figure()
  print(df)
  fig.savefig(f"./graphs/{experiment}-packet-loss")

def graphAvgThroughput(experiment, title, xLabel, yLabel, xValues):
  data = {
    "AODV": [],
    "DSDV": [],
    "OLSR": []
  }

  for protocol in data:
    for dirpath, dirnames, filenames in os.walk(f"{experiment}/{protocol}/csv"):
      for filename in filenames:
        file = os.path.join(dirpath, filename)
        pdr = get_average_throughput(file)
        data[protocol].append(pdr)

  df = pd.DataFrame.from_dict(data)
  df.index = xValues
  fig = df.plot(kind="line", title=title, ylabel=yLabel, xlabel=xLabel, ylim=[0,30]).get_figure()
  print(df)
  fig.savefig(f"./graphs/{experiment}-throughput")

# graphPDR("nodes", "PDR vs Number of nodes", "Number of nodes", "PDR (%)", [20,30,50,70])
# graphPDR("area", "PDR vs Area Simulation", "Area Simulation (m^2)", "PDR (%)", [300,500,1000])
# graphPDR("speed", "PDR vs Speed Simulation", "Speed Simulation  (m/s)", "PDR (%)", [1,2,5,10,20])

# graphPacketLoss("nodes", "Packet Loss vs Number of nodes", "Number of nodes", "Packet Loss (%)", [20,30,50,70])
# graphPacketLoss("area", "Packet Loss vs Area Simulation", "Area Simulation (m^2)", "Packet Loss (%)", [300,500,1000])
# graphPacketLoss("speed", "Packet Loss vs Speed Simulation", "Speed Simulation  (m/s)", "Packet Loss (%)", [1,2,5,10,20])

# graphTransmissionDelay("nodes", "Delay vs Number of nodes", "Number of nodes", "Delay (ms)", [20,30,50,70])
# graphTransmissionDelay("area", "Delay vs Area Simulation", "Area Simulation (m^2)", "Delay (ms)", [300,500,1000])
# graphTransmissionDelay("speed", "Delay vs Speed Simulation", "Speed Simulation  (m/s)", "Delay (ms)", [1,2,5,10,20])

# graphAvgThroughput("nodes", "Throughput vs Number of nodes", "Number of nodes", "Throughput (kbps)", [20,30,50,70])
# graphAvgThroughput("nodesvsreceivers", "Throughput (50% scenario) vs Number of nodes", "Number of nodes", "Throughput (kbps)", [10,20,30,40,50])
graphAvgThroughput("area", "Throughput vs Area Simulation", "Area Simulation (m^2)", "Throughput (kbps)", [300,500,1000])
# graphAvgThroughput("speed", "Throughput vs Speed Simulation", "Speed Simulation  (m/s)", "Throughput (kbps)", [1,2,5,10,20])