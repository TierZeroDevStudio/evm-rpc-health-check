import argparse,json,time,urllib.request
def call(u,m):
 b=json.dumps({"jsonrpc":"2.0","id":1,"method":m,"params":[]}).encode();return json.load(urllib.request.urlopen(urllib.request.Request(u,data=b,headers={"Content-Type":"application/json"}),timeout=8))["result"]
def check(u,caller=call):
 t=time.perf_counter()
 try:return {"ok":True,"chain_id":int(caller(u,"eth_chainId"),16),"block":int(caller(u,"eth_blockNumber"),16),"latency_ms":round((time.perf_counter()-t)*1000,1)}
 except Exception as e:return {"ok":False,"error":str(e),"latency_ms":round((time.perf_counter()-t)*1000,1)}
def main():
 p=argparse.ArgumentParser();p.add_argument("endpoints",nargs="+");a=p.parse_args();r=[dict(endpoint=u.split("?")[0],**check(u)) for u in a.endpoints];print(json.dumps(r,indent=2));raise SystemExit(any(not x["ok"] for x in r))
if __name__=="__main__":main()
