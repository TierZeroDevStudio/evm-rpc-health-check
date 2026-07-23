import unittest
from evm_rpc_health import check
class T(unittest.TestCase):
 def test(self):
  d={"eth_chainId":"0x1","eth_blockNumber":"0x10"};self.assertEqual(check("x",lambda u,m:d[m])["block"],16)
