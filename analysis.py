import pandas as pd
from lxml import objectify

def get_average_throughput(filepath):
  df = pd.read_csv(filepath)
  return df[df['ReceiveRate'] > 0]["ReceiveRate"].mean()


def xml_to_pandas_df(filepath):
  xml_data = objectify.parse(filepath)
  root = xml_data.getroot()
  flow_stats = root.getchildren()[0]
  
  data = []
  cols = flow_stats.getchildren()[0].keys()
  for flow in flow_stats.getchildren():
    attributes = []
    for attribute in flow.attrib.values():
      try:
        attribute = int(attribute)
        attributes.append(attribute)
      except ValueError:
        attributes.append(attribute)
    data.append(attributes)

  df = pd.DataFrame(data) # Write in DF and transpose it
  df.columns = cols  # Update column names
  return df


def get_packet_delivery_ratio(filepath):
  df = xml_to_pandas_df(filepath)
  df["PDR"] = df.rxPackets.div(df.txPackets)
  return df["PDR"].mean()
