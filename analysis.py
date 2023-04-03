import pandas as pd

def get_average_throughput(filepath):
  df = pd.read_csv(filepath)
  return df[df['ReceiveRate'] > 0]["ReceiveRate"].mean()
